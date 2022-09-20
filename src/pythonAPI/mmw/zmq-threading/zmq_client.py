#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
import json

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print("Sending request %s …" % request)
    #socket.send(b"Hello")
    param = {"Actual_fc":"96000000000","Actual_gain":"-200"}
    socket.send_string("Test Command", zmq.SNDMORE)  # send message
    socket.send_string(json.dumps(param, indent=2), zmq.SNDMORE)  # send parameters flattened to json
    # self.sock.send_string(str(data.dtype), zmq.SNDMORE) # send datatype
    # self.sock.send_string(typ, zmq.SNDMORE)  # send datatype
    socket.send_string("data-string")

    #  Get the reply.
    #message = socket.recv()
    message = socket.recv_multipart()
    print("Received reply %s [ %s ]" % (request, str(message)))