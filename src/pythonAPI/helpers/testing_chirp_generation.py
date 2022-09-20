# Generate Waveforms
import helpers

import pathlib
script_dir = pathlib.Path(__file__).parent.resolve()
print(script_dir)
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import mmw
import numpy as np

wfm = helpers.waveform_helpers()
#waveform, attribs = wfm.get_waveform(31e4)  # 1ms@3GSps -> 66e5 pts -> ~13MB
#print(type(waveform))

w = mmw.mmw_helpers.waveform_utilities()
#waveform = w.convert_array_type(waveform, np.int16 )
#print(type(waveform))

Isignal, Qsignal = wfm.generate_chirp_v1(100, 80)
# print(Qsignal)
# print(Isignal)

fs = 3.072e9
length_sec = 1e-6
intleaved = wfm.generate_waveform(fs, helpers.waveform_types.cw, helpers.waveform_datatypes.interleaved_iq, length_sec)
#ToDo: intleaved will be empty
print(intleaved)