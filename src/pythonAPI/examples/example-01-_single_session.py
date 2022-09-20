"""Example for NI mmW Test System and its LabVIEW driver

In this example commands are sent via ZMQ channel for a single Instrument (SystemA only)

Author(s): NOFFZ Technologies GmbH, Vuk Obradovic and Peter Vago, 2020

"""

import pathlib
script_dir = pathlib.Path(__file__).parent.resolve()
print(script_dir)
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from helpers import helpers
from helpers import instr_functions as ins
import time
from mmw import mmw
from mmw import mmw_helpers

# Enable logging
import logging
LOGGINGLVL=logging.INFO # This can be overriden in runtime by using -d option (e.g. -dbug, -ddebug, -derr, -dwarn etc.)
#logbasepath="C:\\ProgramData\\Noffz\\"
logbasepath="log/"
logfile=logbasepath+"testing_nimmW.log"
l = helpers.logging_extra(logfile, LOGGINGLVL)
logger = l.getlogger_reference() #Create object and then Get object reference
#l.change_debuglevel(logging.DEBUG) # Optional, change debuglevel, at any time any any place in the code


def main():
    hostA="192.168.189.120"
    #hostA="127.0.0.1"
    hostB="192.168.189.122"
    #hostB="127.0.0.1"

    global instr
    i = mmw.ni_mmw(hostA) # port is optional. Default instr port is 5555 and 5558. It is set in mmw_config.py
    instr = i


    # Generate Waveforms
    wfm = helpers.waveform_helpers()
    waveform, attribs = wfm.get_waveform(31e4)  # 1ms@3GSps -> 66e5 pts -> ~13MB

    print(i.get_instrument_status())
    i.initialize_hw(mmw.const.opmodes.RF)

    fs = 3.072e9
    i.configure_fs(fs, mmw.const.ports.rx) # Set Fs, can be set to all
    i.configure_fs(fs, mmw.const.ports.tx) # Set Fs, can be set to all


    fc = 75e9  # 76.2 GHz
    i.configure_rf(fc, -10, mmw.const.ports.tx) # gain = -10dB
    i.configure_rf(fc, 10, mmw.const.ports.rx) #gain = 10dB

    i.write_tx("iqsine2", waveform)  # Download waveform to instrument

    i.start(["iqsine2"], 8e-6, 5000)  # burst_name, length in s (10e-6 : 10us)

    # Trigger burst(s)
    i.send_trigger(mmw.const.burst_mode.burst)

    # Single-threaded fetch()
    r, data = i.fetch()  # data is a tuple (data, type<str>)
    print("Response: %s"%str(r))
    print("Data received. Length: %d. Content (chunked): %s ()"%(len(data),str(data[0:100])))
    #Stop
    i.stop()

    # =====================
    print("--- END ---")

    #Plot waveform
    wfm.draw_wfm(data, "Received waveform")
    wfm.show_wfm()



if __name__ == "__main__":
    main()

# =======================
def example_usrp():
    """Example from Barkhausen Inst."""
    # rf_conf = bi_usrp.rf_config() # change this to adjust radio frequency parameters (e.g. sampling frequency)
    # rf_conf.sampling_rate_sps = 10*10**6
    # rf_conf.rf_frequency_hz = 3.75 * 10**9
    # rf_conf.tx_power_dbm = 10
    # (usrp_tx, usrp_rx) = bi_usrp.setup_devices(ip_usrp_tx,ip_usrp_rx, rf_conf)
    # rx_signal = bi_usrp.transmit(usrp_tx, usrp_rx, tx_signal)
    # usrp_tx.disconnect()
    # usrp_rx.disconnect()