'''In this example the single tone signal is generated and transmitted over air using
USRP-2974 device and bi_usrp API.'''

import pathlib
import sys
script_dir = pathlib.Path(__file__).parent.resolve()
print(script_dir)


import logging
import getopt

# Initialize logger
logformat = "%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s" # or '%(levelname)s:%(message)s'
datefmt = "%m-%d %H:%M"
logging.basicConfig(filename="mmW.log" , format=logformat,level=logging.DEBUG, filemode="a", datefmt=datefmt)
stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setFormatter(logging.Formatter(fmt=logformat, datefmt=datefmt))
mylogger = logging.getLogger("mmW")
mylogger.addHandler(stream_handler)

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import mmw

def generate_waveform(en_plot="disabled"):
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

def main():
    ip_usrp_tx = '127.0.0.1'
    ip_usrp_rx = '127.0.0.1'
    host="127.0.0.1"
    port=5558

    from mmw import mmw
    instr = mmw.ni_mmw(host, port)


    code, info = instr.initialize_hw()
    # code, info = instr.reset_application()      # command without any parameter
    # print(code, info)
    #code, info = instr.set_tx_feq(1000001) # sending all data types to server
    instr.configure_trigger()
    instr.configure_rx_sync()
    signal_name= "example_signal"
    fs=3072000000 # Hz
    data = 0
    instr.store_waveform(signal_name, fs, data)
    instr.transceive()

    print("Return Code: %d, Info: '%s'"%(code, info))
    #
    # #send waveform
    wfm = generate_waveform("disabled") # params: plot: "disabled"/<else>, returns a type: numpy.ndarray
    #code, info = instr.store_waveform("test_sine", 1000, wfm) # Waveform_name:str, Fs[Hz]: float, samples:numpy.ndarray
    # code, info, dict = instr.get_all_settings() # request to retrieve all settings
    # print(code, info, dict)





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

if __name__ == "__main__":
    main()