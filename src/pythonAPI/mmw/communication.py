global version

version="ver. 2020-02-24"

import zmq
import sys, os
import json
import logging
import time # for perf measurements
logger=logging.getLogger("mmW")

from enum import Enum

class message_types(Enum):
    """Message types"""
    generic = 0
    response_generic = 1
    response_timout = 2
    response_error = 3

class Errcode(Enum):
    """Error code that is sent in responses and set by the sender"""
    OK = 0
    WARN = 1
    CRIT = 2
    UNKN = 3

class mylock():
    lock = False
    def __init__(self):
        self.lock = False
    def set(self):
        self.lock=True
    def get(self):
        return self.lock
    def reset(self):
        self.lock = False
    def wait_until_is_False(self):
        while self.lock !=0:
            time.sleep(8e-4)
        return self.lock


class communication(object):
    """Communication module

     Abstraction of using whatever channel, e.g pure TCP/IP, ZMQ sub-pub, ZMQ REQ-REP or else..

     Attributes:
         None: this is the main parent class
     """
    sock=""
    snd_lock = 0
    rcv_lock = 0

    def __init__(self, host, port, session_name, recv_to_ms=5000, send_to_ms=5000):
        pass

    def get_version(self):
        return version

    def create_listener(self):
        pass

    def connect_to_listener(self, host, port, session_name, recv_to_ms=5000, send_to_ms=5000, protocol="tcp", pattern="REQREP"):
        """

        @param host: Hostanem or IPaddress
        @param port:
        @param session_name:
        @param recv_to_ms:
        @param send_to_ms:
        @param protocol:
        @param pattern:
        @return:
        """

        pass

    def lock(self, operation="get",direction = "snd"):
        if operation == "get":
            if direction == "snd":
                return self.snd_lock
            else:
                return  self.rcv_lock
        elif operation == "set":
            if direction == "snd":
                self.snd_lock = 1
            else:
                self.rcv_lock = 1
        else:
            if direction == "snd":
                self.snd_lock = 0
            else:
                self.rcv_lock = 0

class comm_zmq(communication):
    """Communication module, ZMQ *

     Abstraction of using whatever channel, e.g pure TCP/IP, ZMQ sub-pub, ZMQ REQ-REP or else..

     Attributes:
         None: this is the main parent class
     """
    shared_context = list() # list type, because we want to share it between mutliple instances. See: https://stackoverflow.com/questions/9751554/list-as-a-member-of-a-python-class-why-is-its-contents-being-shared-across-all
    sockets = list()

    def __init__(self, host, port, session_name, recv_to_ms = 5000, send_to_ms = 5000 ):
        socketopts = dict()
        self._create_context() # Creates Context only once that it will be shared between instances
        self.host = host
        self.port = port
        self.recv_timeout_ms = recv_to_ms  # ms
        self.send_timeout_ms = send_to_ms  # ms
        self.connect_to_listener(host, port , session_name, recv_to_ms, send_to_ms, "tcp", "REQREP")

    def connect_to_listener(self, host,port, session_name,  recv_to_ms = 5000, send_to_ms = 5000, protocol="tcp", pattern="REQREP"):
        """Connecting to a ZMQ listener (to server)

        :param host:
        :param port:
        :param session_name:
        :param recv_to_ms:
        :param send_to_ms:
        :param protocol:
        :param pattern:
        :return:
        """

        self.recv_timeout = recv_to_ms
        self.send_timeout = send_to_ms

        # https://zeromq.org/languages/python/
        logger.debug("RECV_TO: %s, SEND_TO: %d"%(recv_to_ms, send_to_ms))
        #try:

        #  Socket to talk to server
        logger.debug("========== Connecting to server %s on port %s …"%(host, port))
        self.sock = self.context.socket(zmq.REQ)  # Create REQUEST endpoint - Client
        self.sock.setsockopt(zmq.RCVTIMEO, self.recv_timeout_ms)  # set socket option: receive timeout
        self.sock.setsockopt(zmq.SNDTIMEO, self.send_timeout_ms)  # set socket option: send timeout
        socketstring = "%s://%s:%s" % (protocol, host, port)  # "tcp://localhost:5555"
        self.sock.connect(socketstring)  # connect to server (LV vi)
        self.sockets.append(session_name)
        return 0, "OK"
        # except:
        #     info = sys.exc_info()[1]
        #     return 2, info

    def construct_multipart_message(self, typ = message_types.response_error):
        """Construct multipart messages based on defined type.
        MP message: 3-elements list.
            - element 1: "resp:<Errcode>:nocommand" # encoded
            - element 2: {} # Empty JSON string     # encoded
            - element 3: "" # Empty string, encoded
        """

        command = "resp:%s:nocommand"%(str(Errcode.UNKN))
        params, data = {"datatype":"none"}, ""

        message = [command.encode(), json.dumps(params).encode(),data.encode()]

        return message

    def _create_context(self):
        """Creates Context only once that it will be shared between instances

        :return: 0 or exception
        """
        #print(len(self.shared_context))
        if len(self.shared_context) > 1:
            raise Exception("Too many Context: %d"%len(self.shared_context))
        if not self.shared_context:
            #print("Create context")
            self.shared_context.append(zmq.Context())
        self.context = self.shared_context[0]
        return 0

    def create_listener(self, port=55055):
        context = zmq.Context()
        self.sock_listener = context.socket(zmq.REP)
        bind_address = "tcp://*:%s"%(port) # e.g. tcp://*:55055
        logger.debug("Try closing first...")
        # try:
        #     info = self.sock_listener.close()
        # except:
        #     info = sys.exc_info()
        # logger.debug("Closing listener socket: '%s'"%str(info))

        #self.sock_listener.close()
        try:
            bind_address = "tcp://*:55058"
            logger.debug("Starting listener: %s, "%(bind_address))
            #logger.info("---")
            status = self.sock_listener.bind(bind_address)
            #logger.info("---")
            info = "Listener has been created successfully."
            logger.info(info)
            #self.sock_listener.close()
            return 0, info
        except:
            info = sys.exc_info()[1]
            #self.sock_listener.close()
            return 2, info

    def destroy_listener(self):
        """
        Destroy Listener.
        :return:
        """
        info = self.sock_listener.close()
        return 0, info

    def process_status_multipart(self,status):
        """

        :param status:
        :return:
        """
        status2 = []
        try:
            logger.debug(type(status))
            #print(type(status), len(status))
            print(status)

            # for i in status:
            #     i_decoded=i.decode()
            #     print(type(i_decoded))
            #     print(str(i_decoded))

            for k in status:
                print(status.index(k))
                if status.index(k) == 0:
                    status2.append(str(status[status.index(k)].decode()))
                elif status.index(k) == 1:
                    status2.append(str(status[status.index(k)].decode()))
                elif status.index(k) == 2:
                    status2.append(str(status[status.index(k)].decode()))
                elif status.index(k) == 3:
                    status2.append(str(status[status.index(k)].decode()))
                else:
                    pass

            for i in status2:
                print(type(i))
                print(i)
            print(status2)
            return status2
        except:
            info = sys.exc_info()[1]
            status2.append(str(info))
            return status2

    def read_listener(self):
        message = self.sock_listener.recv_multipart()
        # ToDo: do some basic integrity check
        return message

    def read_response(self):
        while self.lock("get","rcv") !=0:
            time.sleep(8e-4)
        self.lock("set","rcv")
        code= 0
        try:
            response = self.sock.recv_multipart()
            logger.debug(response)
            code = 0
        except:
            #ToDo : make it multipart -typed
            response = "No response from %s. Reason: %s"%(self.host,sys.exc_info()[1])
            logger.error(response)
            raise Exception(response)
            response = self.construct_multipart_message(message_types.generic)

            code = 2

        #ToDo: process response according to its type
        # e.g. status2 = self.process_status_multipart(status)
        #logger.debug("REceived response:%s"%str(response))
        self.lock("reset","rcv")
        return code, response

    def set_socket_timeout(self, recv_to, send_to):
        self.recv_timeout = recv_to
        self.send_timeout = send_to
        self.sock.setsockopt(zmq.RCVTIMEO, self.recv_timeout)  # set socket option: receive timeout
        self.sock.setsockopt(zmq.SNDTIMEO, self.send_timeout)  # set socket option: send timeout

    def send_command(self, command, param):
        """Sending pure command without any data. This function translates dictionary to JSON string.

        :param command:
        :param param:
        :return:
        """



        while self.lock("get","snd") !=0:
            time.sleep(8e-4)
        self.lock("set","snd")
        start = time.perf_counter()
        try:
            typ = "none"
            data=0
            #typ = str(type(data)).split('\'')[1].split('\'')[0] # float
            # self.sock.send_string(command)         #send message
            self.sock.send_string(command, zmq.SNDMORE)  # send message
            self.sock.send_string(json.dumps(param, indent=2), zmq.SNDMORE)  # send parameters flattened to json
            # self.sock.send_string(str(data.dtype), zmq.SNDMORE) # send datatype
            #self.sock.send_string(typ, zmq.SNDMORE)  # send datatype

            self.sock.send_string(str(data))
            # self.sock.send(data.tobytes())                      # flatten numpy array to bytes and send it
            #status = self.sock.recv_string()  # retrieve status string
            end = time.perf_counter()
            status = 0
            datasize=len(str(data))
            info = "Data has been sent (%d Bytes)"%datasize
            logger.debug("HOST: %s, CMD: %s, %s (sndtime: %f ms) (sent data: %d B)"%(self.host, command, str(param),(end-start)*1000,datasize))

        except:
            status = 2
            info = sys.exc_info()[1]
            logger.error(sys.exc_info())
        #print(status)
        #logger.debug(type(status))
        #status2 = self.process_status_multipart(status)
        self.lock("reset","snd")
        return status , info

    def send_waveform(self, command, param, data):
        """Sending waveform (and command and parameters)
        :param param:
        :param data:
        :return:
        """
        while self.lock("get","snd") !=0:
            time.sleep(8e-4)
        self.lock("set","snd")
        try:
            #typ = "float"
            #typ = str(type(data)).split('\'')[1].split('\'')[0] # float
            # self.sock.send_string(command)         #send message
            start = time.perf_counter()
            flattendata = data.tobytes()
            end = time.perf_counter()

            self.sock.send_string(command, zmq.SNDMORE)  # send message
            #param["datatype"] = typ
            self.sock.send_string(json.dumps(param, indent=2), zmq.SNDMORE)  # send parameters flattened to json
            self.sock.send(flattendata)                      # flatten numpy array to bytes and send it

            datasize=len(str(data))
            #logger.debug("Command has been sent: %s, %s (time: %f ms) (data: %d B)"%(command, str(param),(end-start)*1000,datasize))
            logger.debug("HOST: %s, CMD: %s, %s (sndtime: %f ms) (sent data: %d B)"%(self.host, command, str(param),(end-start)*1000,datasize))

            #status = self.sock.recv_string()  # retrieve status string
            #status = self.sock.recv_multipart()

            status="OK. Command and Waveform has been sent: %s, %s" % (command, str(param))
        except:
            status = sys.exc_info()[1]
        #print(status)

        self.lock("reset","snd")
        return status

    def write_listener(self, message):
        """Write listener.

        @param message:  text
        @return:  integer code
        """

        logger.debug("-------------------")
        logger.debug(type(message))

        # # if type(message) == array:
        #     k = len(message)
        #     for str in message:
        #         self.sock.send_string(str, zmq.SNDMORE)
        #     #self.sock_listener.send()

#Deprecated methods

    def _depr_send_float(self,command,param, data):
        """Sending float data - Epytext docstring format -

        @param command:
        @param param:
        @param data:
        @return:
        """

        try:
            typ = "float"
            typ = str(type(data)).split('\'')[1].split('\'')[0] # float
            # self.sock.send_string(command)         #send message
            self.sock.send_string(command, zmq.SNDMORE)  # send message
            self.sock.send_string(json.dumps(param, indent=2), zmq.SNDMORE)  # send parameters flattened to json
            # self.sock.send_string(str(data.dtype), zmq.SNDMORE) # send datatype
            self.sock.send_string(typ, zmq.SNDMORE)  # send datatype
            self.sock.send_string(str(data))
            # self.sock.send(data.tobytes())                      # flatten numpy array to bytes and send it
            #status = self.sock.recv_string()  # retrieve status string
            status = self.sock.recv_multipart()
        except:
            status = sys.exc_info()[1]
        #print(status)
        logger.debug(type(status))
        status2 = self.process_status_multipart(status)
        return status2
