

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from mmw import mmw


from helpers import instr_functions as ins
import time
from mmw import mmw_helpers

#def generate_sine()

def generate_sinewave_by_helpers():
    from helpers import helpers
    wfm_name = "Sinewave_01"
    k = 1
    wfmname = "%s%d" % (wfm_name, k)
    # Generate Waveforms
    wfm = helpers.waveform_helpers()
    baselength = 10e4 / 1
    length_pts = int(((k % 10) + 1) * baselength)
    length_pts = 61e3  # 1ms: 615e4
    waveform, attribs = wfm.get_waveform(length_pts)  #
    #fs = 3.072e9
    #length_sec = 80e-6
    #waveform = wfm.generate_waveform(fs , helpers.waveform_types.cw, helpers.waveform_datatypes.interleaved_iq, length_sec)

    print("TX Wavefrom Length :%d" % len(waveform))

    wfm.draw_wfm(waveform, "Waveform from instrument")
    wfm.show_wfm()


def main():
    pass
    # Test1 - using helpers.py - Very simple CW IQ, defined by number of points
    #generate_sinewave_by_helpers()

    # Test2 - using mmy_helpers.py
    #ToDO: This is not implemented. Let's continue with this one.

if __name__ == "__main__":
    main()