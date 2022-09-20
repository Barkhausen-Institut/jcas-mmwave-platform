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

# Enable logging
import logging
LOGGINGLVL=logging.INFO # This can be overriden in runtime by using -d option (e.g. -dbug, -ddebug, -derr, -dwarn etc.)
logbasepath="C:\\ProgramData\\Noffz\\"
logfile=logbasepath+"testing_nimmW.log"
l = helpers.logging_extra(logfile, LOGGINGLVL)
logger = l.getlogger_reference() #Create object and then Get object reference
#l.change_debuglevel(logging.DEBUG) # Optional, change debuglevel, at any time any any place in the code


def main():
    hostA="192.168.40.126"
    portA=5555
    hostB="192.168.40.171"
    portB=5555

    global instr
    instr = mmw.ni_mmw(hostA, portA)

    for i in range(0,1):
        print("Loop test is running. \n ..wait 5 seconds...")
        time.sleep(1)
        start_all = time.perf_counter()
        ins.s01_init_hw(instr)

        # Set Fs
        ins.s02_conf_fs(instr)

        # Set RF
        ins.s03_conf_rf(instr)

        # Synhronization
        ins.s04_conf_sync(instr)

        # Equalization
        #ins.s05_equalization(instr)

        # Generate and download TX waveform
        ins.s06_writeTX(instr)

        #Start generation
        ins.s07_start(instr)

        #Trigger burst(s)
        ins.s08_trigger_burst(instr)

        #Stop
        ins.s09_stop(instr)

        # =====================
        print("--- END ---")
        stop_all = time.perf_counter()
        print("====== Full code Duration: %f sec "%(stop_all - start_all))

        #Plot waveform
        w = ins.show_wfm()
        w.show()




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