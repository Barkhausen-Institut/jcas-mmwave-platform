#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

def evaluate_received_command(message):
    print(type(message))
    cmd     = message[0].decode()
    params  = message[1].decode()
    data    = message[2].decode()

    return 0, cmd, params, data



k = 0
while True:
    #  Wait for next request from client
    #message = socket.recv()
    message = socket.recv_multipart() # Blocking...
    print("Received request: %s" % str(message))

    param = {"Actual_fc":"96000000000","Actual_gain":"-100"}


    if message:
        k = 0

        #Process received data
        retcode, cmd, params, data = evaluate_received_command(message)

        # Send response
        resp_cmd = "OK: %s"%cmd
        socket.send_string(resp_cmd, zmq.SNDMORE)  # send message
        socket.send_string(json.dumps(param, indent=2), zmq.SNDMORE)  # send parameters flattened to json
        # self.sock.send_string(str(data.dtype), zmq.SNDMORE) # send datatype
        # self.sock.send_string(typ, zmq.SNDMORE)  # send datatype
        socket.send_string("response-data")

    #  Do some 'work'
    time.sleep(1)
    k+=1
    print("...%d"%(k))

    #  Send reply back to client
    #socket.send(b"World")