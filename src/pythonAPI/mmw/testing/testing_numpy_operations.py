
import sys
import os.path
import numpy as np

# Import mmw_helpers module from parent path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir  = os.path.abspath(os.path.join(current_dir, os.pardir))
#print(parent_dir)
sys.path.append(parent_dir)
import mmw_helpers as h


w = h.waveform_utilities()
perf = h.performance()

re, im= w.static_re_im_int16()
time=w.get_time(0.1, len(re)) # dt, num_of_samples
#print(len(re))
#time=
#w.plot_real(time, re, "Real sinewave 3")
#w.plot_real(time, im, "Real sinewave 4")

points = 10e6
recordname = '{:.1E}'.format(points)
perf.reset("singen")
c= w.get_interleaved_np_array(points)
perf.record_diff("singen","fullgen_%s_pts"%recordname)
print("len c : %d"%len(c))
print(perf.read("singen"))


time=w.get_time(0.1, len(c)) # dt, num_of_samples
#w.plot_real(time, c, "Real sinewave Interleaved")

#w.plot_re_im(time, c, c, title="Re_Im Wfms")
#w.plot_interlaved_iq(c, "I-Q Waveform")
#w.simple_subplots()

# Plot only at the end of the code.




w.show()

if __name__ == "__main__":
    main()