import typing
import numpy as np
import unittest
from collections.abc import Iterable

import mmw.mmw as mmw
from helpers import helpers

OpMode = mmw.const.opmodes
TriggerMode = mmw.const.burst_mode


def norm_complex(data):
    """Normalize vector of complex values to maximum value (from real or imaginary parts)"""
    data = np.array(data)
    return data / max(max(abs(data.real)), max(abs(data.imag)))


class FrozenBoundedClass(object):
    __is_frozen = False

    def __setattr__(self, key, value):
        if hasattr(self.__class__, "bounds",):
            bounds = getattr(self.__class__, "bounds",)
            if key in bounds:
                if value > bounds[key][1] or value < bounds[key][0]:
                    raise ValueError(
                        str(value)
                        + " is out of bounds: ("
                        + str(bounds[key][0])
                        + ", "
                        + str(bounds[key][1])
                        + ")"
                    )
        if self.__is_frozen and not hasattr(self, key):
            raise KeyError("%r is a frozen class" % self)
        object.__setattr__(self, key, value)

    def _freeze(self):
        self.__is_frozen = True


def setup_p2p_devices(
    ip_tx: str, ip_rx: str, rf_config=None, enable_sync=True, enable_LO_sync=True
):
    """connects to USRPs and setups RF parameters. If rf_config is not defined
    default parameters are used.
    """
    instr_tx = setup_device(
        ip_tx,
        rf_config=rf_config,
        enable_LO_sync=enable_LO_sync,
        enable_sync=enable_sync,
    )
    if ip_tx != ip_rx:
        instr_rx = setup_device(ip_rx, rf_config)
    else:
        instr_rx = instr_tx
    return (instr_tx, instr_rx)


def setup_device(
    ip: str, rf_config=None, enable_sync=True, enable_LO_sync=True, timeout=60
):
    instr = mmw.ni_mmw(ip)
    # Synchronization
    instr.trigger_sync_enable(enable_sync)
    instr.enable_LO_sync(enable_LO_sync)
    if rf_config is None:
        instr.initialize_hw(OpMode.RF, timeout=timeout * 1000)
    else:
        instr.initialize_hw(rf_config.op_mode, timeout=timeout * 1000)
        instr.configure_fs(fs=rf_config.sampling_rate_sps, port=mmw.const.ports.all)
        instr.configure_rf(  # configure TX
            fc=rf_config.rf_frequency_hz,
            gain=rf_config.tx_power_dbm,
            port=mmw.const.ports.tx,
        )
        instr.configure_rf(  # configure RX
            fc=rf_config.rf_frequency_hz,
            gain=rf_config.rx_gain_dbm,
            port=mmw.const.ports.rx,
        )
    return instr


def _single_device_transmition(
    instr, wfmname, length_to_receive_sec, timeout_ms, trigger_mode
):
    instr.start([wfmname], length_to_receive_sec, timeout_ms)
    instr.send_trigger(trigger_mode)
    rx_info, rx_data = instr.fetch()
    return _from_send_type(rx_data)


def _multi_device_transmition(
    instr_tx,
    instr_rx_list,
    wfmname,
    length_to_receive_sec_list,
    timeout_ms,
    trigger_mode,
):
    # multi session
    inst_rx_list = [
        (instr_rx, [wfmname], length_to_receive_sec, timeout_ms)
        for instr_rx, length_to_receive_sec in zip(
            instr_rx_list, length_to_receive_sec_list
        )
    ]
    start_arg_list = [
        (instr_tx, [wfmname], length_to_receive_sec_list[0], timeout_ms),
        *inst_rx_list,
    ]
    mmw.start_multi(start_arg_list)
    instr_tx.send_trigger(trigger_mode)
    for instr_rx in instr_rx_list:
        if instr_rx != instr_tx:
            instr_rx.send_trigger(TriggerMode.continuous)

    rx_data = [_from_send_type(instr_rx.fetch()[1]) for instr_rx in instr_rx_list]
    return rx_data


def transmit(
    instr_tx,
    instr_rx,
    tx_signal,
    length_to_receive_sec=None,
    timeout=4,
    trigger_mode=TriggerMode.burst,
):
    wfmname = "tx_signal_from_python_api"
    instr_tx.write_tx(
        wfmname, _to_send_type(tx_signal)
    )  # Download waveform to instrument
    timeout_ms = timeout * 1000
    if isinstance(instr_rx, Iterable):
        #print(" multi session multiple receiver")
        if isinstance(length_to_receive_sec, Iterable):
            length_to_receive_sec_list = length_to_receive_sec

        else:
            length_to_receive_sec_list = [length_to_receive_sec for _ in range(2)]

        return _multi_device_transmition(
            instr_tx=instr_tx,
            instr_rx_list=instr_rx,
            wfmname=wfmname,
            length_to_receive_sec_list=length_to_receive_sec_list,
            timeout_ms=timeout_ms,
            trigger_mode=trigger_mode,
        )
    else:
        if instr_tx == instr_rx:
            #print("Single SESSION")
            return _single_device_transmition(
                instr=instr_tx,
                wfmname=wfmname,
                length_to_receive_sec=length_to_receive_sec,
                timeout_ms=timeout_ms,
                trigger_mode=trigger_mode,
            )
        else:
            # print("multi session single receiver")
            return _multi_device_transmition(
                instr_tx=instr_tx,
                instr_rx_list=[instr_rx],
                wfmname=wfmname,
                length_to_receive_sec_list=[length_to_receive_sec],
                timeout_ms=timeout_ms,
                trigger_mode=trigger_mode,
            )[0]


def _to_send_type(waveform):
    if max(waveform.real.max(), waveform.imag.max()) > 1:
        waveform = norm_complex(waveform) * 32767
    else:
        waveform *= 32767
    i = np.array(waveform.real, dtype=np.int16)
    q = np.array(waveform.imag, dtype=np.int16)
    interleaved = np.empty(waveform.size * 2, dtype=np.int16)
    interleaved[0::2] = q  # work around noffz bug iq
    interleaved[1::2] = i
    return interleaved


def _from_send_type(interleaved_data):
    waveform = (interleaved_data[0::2] + 1j * interleaved_data[1::2]) / 32767
    return waveform


class RfConfig(FrozenBoundedClass):
    """Contains radio frequency configuration for mmW system"""

    def __init__(self):
        #: Sampling Rate [S/s]
        self.sampling_rate_sps = 3.072e9
        #: Local oscillator frequency [Hz]
        self.rf_frequency_hz = 75e9
        self.tx_power_dbm = 10  #: TX power [dBm]
        self.rx_gain_dbm = 10  #: RX (inverted) reference Level [dBm]
        self.op_mode = OpMode.RF  #: Operation mode RF, IF, BB
        self._freeze()
