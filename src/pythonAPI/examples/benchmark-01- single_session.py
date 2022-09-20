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
LOGGINGLVL=logging.DEBUG # This can be overriden in runtime by using -d option (e.g. -dbug, -ddebug, -derr, -dwarn etc.)
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
    i = mmw.ni_mmw(hostB, portB)
    instr = i

    for k in range(0,3):
        # Generate Waveforms
        wfm = helpers.waveform_helpers()
        waveform, attribs = wfm.get_waveform(615e4)  # 1ms@3GSps -> 615e4 pts -> ~13MB

        perf.reset("main")
        i.initialize_hw(mmw.const.instr_hwclass.NI_mmW01, mmw.const.opmodes.RF)
        perf.record_diff("main","01_init_hw")
        fs = 3.072e9
        i.configure_fs(fs, mmw.const.ports.rx) # Set Fs, can be set to all
        i.configure_fs(fs, mmw.const.ports.tx) # Set Fs, can be set to all
        perf.record_diff("main","02_conf_fs")

        fc = 75e9  # 76.2 GHz
        #i.configure_rf(fc, -10, mmw.const.ports.tx) # gain = -10dB
        #i.configure_rf(fc, 10, mmw.const.ports.rx) #gain = 10dB
        perf.record_diff("main","03_conf_rf")

        #ins.s04_conf_sync(instr)       # Synhronization

        #ins.s05_equalization(instr)    # Equalization

        i.write_tx("iqsine7", waveform)  # Download waveform to instrument
        perf.record_diff("main","04_write_tx-1ms")

        i.start(["iqsine7"], 800e-6, 15000)  # burst_name, length in s (10e-6 : 10us)
        perf.record_diff("main","05_start")

        # Trigger burst(s)
        r,data = i._depr_trigger_burst("iqsine", mmw.const.burst_mode.burst)  # 1x iqsine + mode
        perf.record_diff("main","06_trigger_burst")
        #print("Data received: %d"%len(data))

        #print(instr.send_trigger())
        #response , data = instr.fetch() # data is a tuple (data, type<str>)

        #Stop
        i.stop()
        perf.record_abs("main","07_fulltime")



        # =====================
        #print("--- END ---")
        print("[%d]====== performance data: %s "%(k,str(perf.read("main"))))


        #Plot waveform
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