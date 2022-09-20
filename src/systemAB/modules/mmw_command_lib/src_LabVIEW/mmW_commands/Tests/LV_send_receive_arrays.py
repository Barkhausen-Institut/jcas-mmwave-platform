# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:26:25 2019
@author: Vuk
"""

import zmq
import json
import numpy as np
import matplotlib.pyplot as plt


class LVAPI:
    def __init__(self, server: str) -> None:
        self.zmq_context = zmq.Context()
        self.server = server
        self.sock = self.zmq_context.socket(zmq.REQ)  # Create REQUEST endpoint - CLient
        self.sock.setsockopt(zmq.RCVTIMEO, 2000)       # set recieve timeout to 500ms
        self.sock.setsockopt(zmq.SNDTIMEO, 2000)       # set send timeout to 500ms
        self.sock.connect("tcp://" + self.server)     # connect to LabVIEW data server

    def send(self, message: str, parameters: dict, data: np.array) -> str  :
        """

        Args:
            message: string containing message descriptor
            parameters: dictionary with parameters
            data: numpy array with data to be sent

        Returns: status string

        """

        try:
            self.sock.send_string(message,zmq.SNDMORE)  # send message, added flag zmq.SNDMORE to indicate pultipart message
            self.sock.send_string(json.dumps(parameters, indent=2),zmq.SNDMORE)  # send parameters dictiionary flattened to JSON
            self.sock.send_string(str(data.dtype), zmq.SNDMORE)  # send data type
            self.sock.send(data.tobytes())  # flattend numpy array to byte stream
            status = self.sock.recv_string()                 # response is command status: OK or error
        except:
            status = 'zmq_timeout'
        return status

    def retrieve(self, message: str) -> tuple:
        """
        Retrieves data from LabVIEW

        Sends message and waits for status, response, data type and data

        Args:
            message: string containing message

        Returns: status, response as json and data as numpy array

        """
        self.sock.send_string(message)  # send message

        try:

            status = self.sock.recv_string()         # recieve message status
            response_str = self.sock.recv_string()   # recieve response json
            response = json.loads(response_str)      # parse response json into dictionary
            response_type = self.sock.recv_string()  # receive data type
            response_bytes = self.sock.recv()        # recieve data
            data=np.frombuffer(response_bytes, dtype=np.dtype(response_type)) #convert data to numpy array

        except:
            status = 'zmq_timeout'
            response = dict()
            data = np.array(0)

        finally:

            return [status, response, data]
    def close(self):
        self.sock.close()
        self.zmq_context.destroy()

# MAIN CODE



# Open communicaiton to LV
LV = LVAPI("127.0.0.1:5555")

#Prepare config
config = dict()
config["Instrument"] = "Device0"  # Device ID (IVI/RIO resource name)
config["Fs"] = 3e9  # Set Fs rate to 3GHz


# prepare some data
duration=1e-3                                     #10ms burst
fc=2000                                             #sinewave at 200HZ
data_type=np.dtype('float64')                       #specify data type
time = np.linspace(0, duration, num=int(duration*config["Fs"]), dtype=data_type)  #Generate time vector
data_out = np.sin(2* np.pi * fc * time)              #Generate sine wave

# send config and double array array to LV
status = LV.send('set_tx', config, data_out)

#retrieve data from LV
[status,response,data_in]=LV.retrieve('read_rx')
print(status)

#plot response data
plt.plot(data_in)
plt.ylabel('scope data')
plt.show()

#close communication
LV.close()


