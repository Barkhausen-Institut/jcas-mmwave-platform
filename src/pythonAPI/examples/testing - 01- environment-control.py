"""Example for NI mmW Test System and its LabVIEW driver

In this example commands are sent via ZMQ channel to the Environment Control Service (mmWave service application on both Instruments).
That service is responsible to start /restart the Instrument app and return its status.


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
    hostA="192.168.40.170"
    hostB="192.168.40.171"


    global instr
    i = mmw.ni_mmw(hostB)
    instr = i

    print(i.get_instrument_status())


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