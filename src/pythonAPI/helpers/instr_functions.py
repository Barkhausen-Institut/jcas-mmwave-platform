import os, sys, time
# Import mmw_helpers module from parent path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir  = os.path.abspath(os.path.join(current_dir, os.pardir))
#print(parent_dir)
sys.path.append(parent_dir)
mmwdir="%s/mmw"%parent_dir
sys.path.append(mmwdir)
from mmw import mmw

from mmw import mmw_helpers as h
global w
w = h.waveform_utilities()

def get_waveform(points):
    global w
    w = h.waveform_utilities()
    data = w.get_interleaved_np_array(points)
    attribs = w.get_wfm_attributes(data)
    return data, attribs


def draw_wfm(data, title):

    # time = w.get_time(0.1, len(data)-0.5)
    # w.plot_real(time, data, title)
    w.plot_interlaved_iq(data, title)
    #w.show()
    return 0

def show_wfm():
    print("Plotting...")
    w.show()
    return w

def s01_init_hw(i=mmw.ni_mmw("127.0.0.1", "5555")):
    i.initialize_hw(mmw.const.instr_hwclass.NI_mmW01, mmw.const.opmodes.RF)
    #i.initialize_hw()

def s02_conf_fs(i=mmw.ni_mmw("127.0.0.1", "5555")):
    fs = 3.072e9 #max 3.072GHz, 3.072e9
    try:
        response = i.configure_fs(mmw.const.ports.tx, fs)
        print("Response received: %s"%(str(response)))
    except:
        pass
    response = i.configure_fs(mmw.const.ports.rx, fs)
    print("Response received: %s"%(str(response)))
    # response = instrB.configure_fs(mmw.const.ports.rx, fs)
    # print("Response received: %s"%(str(response)))

    # instr.configure_fs(mmw.const.ports.rx, fs)
    # instr.configure_fs(mmw.const.ports.rx, fs)

def s03_conf_rf(i=mmw.ni_mmw("127.0.0.1", "5555")):
    fc = 75e9 # 76.2 GHz
    try:
        gain = -10  # dB
        response = i.configure_rf(mmw.const.ports.tx, fc, gain)
        print("Response received: %s"%(str(response)))
    except:
        pass
    gain = 10 # dB
    response = i.configure_rf(mmw.const.ports.rx, fc, gain)
    print("Response received: %s"%(str(response)))

    # response = instr.configure_rf(mmw.const.ports.tx, fc, gain)
    # print("Response received: %s"%(str(response)))
    # gain = 10 # dB
    # response = instr.configure_rf(mmw.const.ports.rx, fc, gain)
    # print("Response received: %s"%(str(response)))
    # gain = 10 # dB
    # response = instrB.configure_rf(mmw.const.ports.rx, fc, gain)
    # print("Response received: %s"%(str(response)))

    # instr.configure_rf(mmw.const.ports.rx, fc, gain)
    # instr.configure_rf(mmw.const.ports.rx, fc, gain)

def s04_conf_sync(i=mmw.ni_mmw("127.0.0.1", "5555")):
    response = i.trigger_sync_enable(True)
    print("Response received: %s"%(str(response)))
    response = i.enable_LO_sync(True)
    print("Response received: %s" % (str(response)))

    # response = instrA.trigger_sync_enable(True)
    # print("Response received: %s"%(str(response)))
    # response = instrB.trigger_sync_enable(True)
    # print("Response received: %s" % (str(response)))
    # response = instrA.enable_LO_sync(True)
    # print("Response received: %s"%(str(response)))
    # response = instrB.enable_LO_sync(True)
    # print("Response received: %s"%(str(response)))

def s05_equalization(i=mmw.ni_mmw("127.0.0.1", "5555")):
    # response = instr.equalization_enable(True)
    # print("Response received: %s"%(str(response)))
    # response = instr.equalization_start()
    # print("Response received: %s"%(str(response)))
    # time.sleep(20) # Wait 20 seconds before stopping equalization
    # response = instr.equalization_stop()
    # print("Response received: %s"%(str(response)))
    pass

def s06_writeTX(i=mmw.ni_mmw("127.0.0.1", "5555")):
    waveform, attribs = get_waveform(66e5) #66e5

    print("Wfm length: %s"%str(waveform.shape))
    attr={"datatype": mmw.const.datatypes.interleaved_I16.name} # "length" : attribs["length"]}
    #response = i.write_tx("header", waveform, attr)
    start = time.perf_counter()
    response = i.write_tx("iqsine", waveform, attr)
    end = time.perf_counter()
    print("Response received: %s"%(str(response)))
    print("=== Write TX duration: %f"%(end-start))

def s07_start(i=mmw.ni_mmw("127.0.0.1", "5555")):
    response = i.start(["iqsine"], 1000e-6, 15000) # burst_name, length in s (10e-6 : 10us)
    print("Response received: %s"%(str(response)))

    # #response = instr.start(["iqsine_invalid_name"], 10) # burst_name, length in ms
    # response = instr.start(["iqsine"], 500e-6, 15000) # burst_name, length in s (10e-6 : 10us)
    # print("Response received: %s"%(str(response)))


def s08_trigger_burst(i=mmw.ni_mmw("127.0.0.1", "5555")):
    from . import helpers as h

    start , end = 0.1, 0.1
    start = time.perf_counter()
    #response = instr.trigger_burst("iqsine") # 1x iqsine
    #response = instr.trigger_burst(["iqsine", "iqsine"]) # 2x


    response = i.trigger_burst("iqsine", mmw.const.burst_mode.burst) # 1x iqsine + mode
    end = time.perf_counter()
    try:
        #draw_wfm(response["Data"], "Waveform")
        print("Response received: %s" % (str(response)))
    except:
        print("Response TIMEOUT: %s" % (str(response)))
    #print("Response received: %s"%(str(response)))
    print("====== Duration of trigger burst: %f sec "%(end-start))


def s09_stop(i=mmw.ni_mmw("127.0.0.1", "5555")):
    response = i.stop()
    print("Response received: %s"%(str(response)))

