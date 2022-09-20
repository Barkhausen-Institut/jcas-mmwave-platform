"""Example for NI mmW Test System and its LabVIEW driver

In this example commands are sent via ZMQ channel

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
LOGGINGLVL=logging.ERROR # This can be overriden in runtime by using -d option (e.g. -dbug, -ddebug, -derr, -dwarn etc.)
logbasepath="C:\\ProgramData\\Noffz\\"
logfile=logbasepath+"testing_nimmW.log"
l = helpers.logging_extra(logfile, LOGGINGLVL)
logger = l.getlogger_reference() #Create object and then Get object reference
#l.change_debuglevel(logging.DEBUG) # Optional, change debuglevel, at any time any any place in the code

global perf
perf = mmw_helpers.performance()

def main():
    hostA="192.168.40.126"
    portA=5555
    hostB="192.168.40.171"
    hostB="127.0.0.1"
    portB=5555

    global instr
    i = mmw.ni_mmw(hostA, portA)
    instr = i

    range_max = 10
    tx_max = 615e4
    tx_step = tx_max / range_max
    rx_max = 1
    wfm_name="test_"



    for k in range(0,range_max):
        wfmname = "%s%d"%(wfm_name, k)
        # Generate Waveforms
        wfm = helpers.waveform_helpers()
        baselength = 10e4 / 1
        length = int(((k%10)+1) * baselength)
        waveform, attribs = wfm.get_waveform(length)  #
        #print("TX Wavefrom Length :%d"%len(waveform))


        perf.reset("main")
        if k%1 == 0:
                i.initialize_hw(mmw.const.instr_hwclass.NI_mmW01, mmw.const.opmodes.BB , 60000) # This is done automatically . Need to be called when reinit needed.
        else:
                i.initialize_hw(mmw.const.instr_hwclass.NI_mmW01, mmw.const.opmodes.RF , 60000) # This is done automatically . Need to be called when reinit needed.

        perf.record_diff("main","01_init_hw")
        fs = 3.072e9
        fs = fs/1
        #i.configure_fs(fs, mmw.const.ports.rx) # Set Fs, can be set to all
        #i.configure_fs(fs, mmw.const.ports.tx) # Set Fs, can be set to all
        perf.record_diff("main","02_conf_fs")

        if k%1 == 0:
            fc = 10e9
        else:
            fc = 75e9  # 76.2 GHz
        #i.configure_rf(fc, -10, mmw.const.ports.tx) # gain = -10dB
        #i.configure_rf(fc, 10, mmw.const.ports.rx) #gain = 10dB
        perf.record_diff("main","03_conf_rf")

        #ins.s04_conf_sync(instr)       # Synhronization

        #ins.s05_equalization(instr)    # Equalization

        i.write_tx(wfmname, waveform)  # Download waveform to instrument
        perf.record_diff("main","04_write_tx-1ms")

        length = float(((k%10)+1) * 80e-6)
        i.start([wfmname], length, 5000)  # burst_name, length in s (10e-6 : 10us)
        perf.record_diff("main","05_start")

        # Trigger burst(s)
        #r,data = i._depr_trigger_burst("iqsine", mmw.const.burst_mode.burst)  # 1x iqsine + mode

        i.send_trigger(mmw.const.burst_mode.continuous)
        perf.record_diff("main","06_send_trigger")
        r , data = instr.fetch() # data is a tuple (data, type<str>)
        perf.record_diff("main","07_fetch")
        #print("Data received: %d"%len(data))

        #Stop
        i.stop()
        perf.record_abs("main","08_fulltime")



        # =====================
        #print("--- END ---")
        print("[%d]====== performance data: %s "%(k,str(perf.read("main"))))


        #Plot waveform
        #wfm.draw_wfm(data, "Waveform from instrument")
        #wfm.show_wfm()

        #print("Loop test is running. \n ..wait 1 second(s)...")
        time.sleep(1)


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