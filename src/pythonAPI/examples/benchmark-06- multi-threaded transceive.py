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
import random
import _thread

# Enable logging
import logging
LOGGINGLVL=logging.WARNING # This can be overriden in runtime
logbasepath="C:\\ProgramData\\Noffz\\"
logfile=logbasepath+"testing_nimmW.log"
l = helpers.logging_extra(logfile, LOGGINGLVL)
logger = l.getlogger_reference() #Create object and then Get object reference
#l.change_debuglevel(logging.DEBUG) # Optional, change debuglevel, at any time any any place in the code

global perf
perf = mmw_helpers.performance()

def main():
    hostA="192.168.40.170"
    portA=5555
    hostB="192.168.40.171"
    hostB="127.0.0.1"
    portB=5558

    global instr
    iA = mmw.ni_mmw(hostA, portA)
    iB = mmw.ni_mmw(hostB, portB)

    range_max = 1
    tx_max = 615e4
    tx_step = tx_max / range_max
    rx_max = 1
    rnd = random.randrange(10000,99999,2) # even integer between 10e4 and 10e5
    wfm_name="test_%s"%str(rnd)

    for k in range(0,range_max):
        wfmname = "%s%d"%(wfm_name, k)
        # Generate Waveforms
        wfm = helpers.waveform_helpers()
        baselength = 10e4 / 1
        length = int(((k%10)+1) * baselength)
        length = 496e4 # 1ms: 615e4 samples
        waveform, attribs = wfm.get_waveform(length)  #
        print("TX Waveform Length :%d"%len(waveform))


        perf.reset("main")
        iA.initialize_hw(mmw.const.instr_hwclass.NI_mmW01, mmw.const.opmodes.RF , 3000) # This is done automatically . Need to be called when reinit needed.
        #iB.initialize_hw(mmw.const.instr_hwclass.NI_mmW01, mmw.const.opmodes.RF , 3000) # This is done automatically . Need to be called when reinit needed.
        perf.record_diff("main","01_init_hw")


        fsmax = 3.072e9
        fs = fsmax/1
        # Single-threaded configure_fs
        iA.configure_fs(fs, mmw.const.ports.rx) # Set Fs, can be set to all
        iA.configure_fs(fs, mmw.const.ports.tx) # Set Fs, can be set to all
        #iB.configure_fs(fs, mmw.const.ports.rx) # Set Fs, can be set to all
        # Multi-threaded configure_fs
        #conf_fs_list = [(iA, fs, mmw.const.ports.rx),(iA, fs, mmw.const.ports.tx),(iB, fs, mmw.const.ports.rx)]
        #conf_fs_list = [(iA, fs/10, mmw.const.ports.rx),(iA, fs/10, mmw.const.ports.tx),(iA, fs/2, mmw.const.ports.rx),(iA, fs/2, mmw.const.ports.rx),(iA, fs, mmw.const.ports.rx),(iA, fs, mmw.const.ports.rx)]
        #responses = mmw.configure_fs_multi(conf_fs_list)
        perf.record_diff("main","02_conf_fs")

        fc = 75e9  # 76.2 GHz
        #iA.configure_rf(fc, -10, mmw.const.ports.tx) # gain = -10dB
        #iA.configure_rf(fc, 10, mmw.const.ports.rx) #gain = 10dB
        #iB.configure_rf(fc, 10, mmw.const.ports.rx) #gain = 10dB

        perf.record_diff("main","03_conf_rf")

        #ins.s04_conf_sync(instr)       # Synhronization
        #iA.trigger_sync_enable(True)
        #iA.enable_LO_sync(True)
        #iB.trigger_sync_enable(True)
        #iB.enable_LO_sync(True)
        perf.record_diff("main","031_Sync")

        #ins.s05_equalization(instr)    # Equalization
#TRSCV
        # TRSCV - SINGLE THREADED - 470ms
        length = float(((k%10)+1) * 80e-6)
        length = 800e-6 # 1ms
        burst_mode = mmw.const.burst_mode.burst
        timeout = 5000 # ms
        # r, data = iA.transceive(waveform, wfmname, length, burst_mode, timeout) #
        # perf.record_diff("main", "032_Transceive-Single")
        #
        # print("%s \n %d\n %s..Truncated"%(str(r), len(data), str(data[0:10])))


        #TRSCV - MULTI-THREADED - 520ms on 1 thread
        r, data = mmw.transceive_multi([iA, iB],waveform, wfmname, length, burst_mode, timeout)
        perf.record_diff("main", "032_Transceive-multi")
        #print(r, data[0:100])
        try:
         for resp, d in r, data:
            print(resp) # {'Errcode': 'OK', 'Command': 'fetch', 'Parameters': {'generic_info': '', 'datatype': <datatypes.interleaved_I16: 2>, 'source': ''}}
            print("Data length: %d"% len(d)) # Data length: 3072000
        except:
            print("No data returned. %s"%sys.exc_info()[1])

#TRSCV end
#         iA.write_tx(wfmname, waveform)  # Download waveform to instrument
#         #iB.write_tx(wfmname, waveform)  # Download waveform to instrument
#         perf.record_diff("main","04_write_tx-1ms")
#
#
#         # Single-threaded start()
#         #iA.start([wfmname], length, 5000)  # burst_name, length in s (10e-6 : 10us)
#         #iB.start([wfmname], length, 5000)  # burst_name, length in s (10e-6 : 10us)
#         # Multi-threaded start()
#         start_arg_list=[(iA,[wfmname], length, 5000), (iB, [wfmname], length, 5000)]
#         mmw.start_multi(start_arg_list)
#         perf.record_diff("main","05_start")
#
#         # Trigger burst(s)
#         #r,data = i._depr_trigger_burst("iqsine", mmw.const.burst_mode.burst)  # 1x iqsine + mode
#
#         iA.send_trigger(mmw.const.burst_mode.burst)
#         iB.send_trigger(mmw.const.burst_mode.continuous) # Not needed if Synchonization is set. But better to send always, SysB will ignore it...
#         perf.record_diff("main","06_send_trigger")
#
#         # Single-threaded fetch()
#         r , data = iA.fetch() # data is a tuple (data, type<str>)
#         print(r, data[0:100])
#         r , data = iB.fetch() # data is a tuple (data, type<str>)
#         print(r, data[0:100])
#
#         # Multi-threaded fetch()
#
#
#         # r, data = mmw.fetch_multi([(iA,5000),(iB,5000)])
#         # #print(r, data[0:100])
#         # try:
#         #  for resp, d in r, data:
#         #     print(resp) # {'Errcode': 'OK', 'Command': 'fetch', 'Parameters': {'generic_info': '', 'datatype': <datatypes.interleaved_I16: 2>, 'source': ''}}
#         #     print("Data length: %d"% len(d)) # Data length: 3072000
#         # except:
#         #     pass
#         perf.record_diff("main","07_fetch")
#         #print("Data received: %d"%len(data))
# #


        #Stop
        iA.stop()
        iB.stop()
        perf.record_abs("main","08_fulltime")



        # =====================
        #print("--- END ---")
        print("[%d]====== performance data: %s "%(k,str(perf.read("main"))))


        #Plot waveform
        #wfm.draw_wfm(data, "Waveform from instrument")
        #wfm.show_wfm()

        #print("Loop test is running. \n ..wait 1 second(s)...")
        time.sleep(0.3)


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