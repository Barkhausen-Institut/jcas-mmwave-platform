"""
Helper functions for examples
- logging
- waveform creation (more waveform creation helper functions are located in mmw/mmw_helpers.py)
"""

import logging
import sys
import os, sys, time
# Import mmw_helpers module from parent path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir  = os.path.abspath(os.path.join(current_dir, os.pardir))
#print(parent_dir)
sys.path.append(parent_dir)
mmwdir="%s/mmw"%parent_dir
sys.path.append(mmwdir)
from mmw import mmw

import numpy as np

from mmw import mmw_helpers as h
global w
w = h.waveform_utilities()

class logging_extra():
    """Logging class"""
    mylogger = "" # declare only
    recovery_code, recovery_info = 3, "default"

    def __init__(self, logfile="/tmp/mylogger.log", LOGGINGLVL=logging.DEBUG):
        import logging

        ###### nfz_util = noffz_generic_utils()
        ###### self.recovery_code, self.recovery_info = nfz_util.logfile_recovery(logfile) # Logfile writing issue : chown or delete it if not accessible
        #print("%d, '%s'"%(self.recovery_code, self.recovery_info))
        # Initialize logger
        logformat = "%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s"
        datefmt = "%m-%d %H:%M"
        logging.basicConfig(filename=logfile, level=LOGGINGLVL, filemode="a", format=logformat, datefmt=datefmt)
        stream_handler = logging.StreamHandler(sys.stderr)
        stream_handler.setFormatter(logging.Formatter(fmt=logformat, datefmt=datefmt))
        self.mylogger = logging.getLogger("mmW")
        self.mylogger.addHandler(stream_handler)

        #if self.recovery_code != 0: #
        #    self.mylogger.info(self.recovery_info) # if logfile has been chown'ed or deleted or any other issue happened...

    def getlogger_reference(self):
        # Data accessor
        return self.mylogger

    def change_debuglevel(self, newlevel):
        # critical, error, warning, info, debug, notset" # https://docs.python.org/2/library/logging.html
        lvl_list = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"]
        nl = newlevel.upper()
        if any(nl in l for l in
               lvl_list):  # True if nl is matching to any string or ANY SUBSTRING in the list. E.g. "NING" -> WARNING :D
            nl_suppl = [s for s in lvl_list if nl in s]  # Type: list!, Supplements , eg. "WARN" -> "WARNING"
            logging.getLogger().setLevel(nl_suppl[0])
            self.mylogger.debug("newlevel:%s" % nl_suppl)

            if self.recovery_code != 0:  # This is from __init__, but applying new loglevel...hacking, I know..
                self.mylogger.info(self.recovery_info)  # if logfile has been chown'ed or deleted or any other issue happened...

            return 0
        else:
            print("Debug level is invalid: '%s' (expected: %s) /non case-sensitive/" % (newlevel, str(lvl_list)))
            return 23


class waveform_helpers():
    """Waveform helper functions for exmaples"""

    def __init__(self):
        global w
        w = h.waveform_utilities()

    def get_waveform(self,points):

        data = w.get_interleaved_np_array(points)
        attribs = w.get_wfm_attributes(data)
        return data, attribs

    def draw_wfm(self, data, title):
        # time = w.get_time(0.1, len(data)-0.5)
        # w.plot_real(time, data, title)
        w.plot_interlaved_iq(data, title)
        # w.show()
        return 0

    def show_wfm(self):
        print("Plotting...")
        w.show()
        return w

    def generate_sinewave_real(self, en_plot="disabled"):
        """
        https://pythontic.com/visualization/charts/sinewave
        :return:
        """
        import numpy as np
        import matplotlib.pyplot as plot

        # Get x values of the sine wave
        time = np.arange(0, 100, 0.1);
        # Amplitude of the sine wave is sine of a variable like time
        amplitude = np.sin(time)
        if en_plot != "disabled":
            # Plot a sine wave using time and amplitude obtained for the sine wave
            plot.plot(time, amplitude)
            # Give a title for the sine wave plot
            plot.title('Sine wave')
            # Give x axis label for the sine wave plot
            plot.xlabel('Time')
            # Give y axis label for the sine wave plot
            plot.ylabel('Amplitude = sin(time)')
            plot.grid(True, which='both')
            plot.axhline(y=0, color='k')
            plot.show()
            # Display the sine wave
            plot.show()
        return amplitude



