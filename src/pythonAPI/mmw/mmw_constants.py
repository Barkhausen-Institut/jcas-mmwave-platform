from enum import Enum

class opmodes(Enum):
    """Operational modes: Baseband, IF-Intermediate Frequency, RF-microwave radio frequency"""
    BB = 0
    IF = 1
    RF = 2

class ni_mmw_modes(Enum):
    """Not used. opmodes used instead. (in versions 2020-04-06 or later)"""
    BB = 0
    IF = 1
    RF = 2

class hw_state(Enum):
    """Instrument hardware status. get_config command returns its value"""
    Off             =   0
    Configuration   =   1
    Running         =   2
    Calibration     =   3
    Unknown         =   4

class ports(Enum):
    """ 'rx', 'tx', 'all' """
    rx = 0
    tx = 1
    all = 2

class lo1_sharing(Enum):
    """Modes of sharing the LO1 (local osc. #1)"""
    Disabled = 0
    Export = 1
    Import = 2

class lo2_sharing(Enum):
    """Modes of sharing the LO2 (local osc. #2)"""
    Disabled = 0
    Export = 1
    Import = 2

class instr_hwclass(Enum):
    """Instrument hardware class. Makes it possible to define multiple hw types and/or software versions, or even simulated hardware."""
    Simulated = 0
    NI_mmW01 = 1
    Other = 2

class trigger_source(Enum):
    """Trigger Source options: T-CLock or PXI-Trigger"""
    Tclk     = 0
    PXI_Trig = 1

class trigger_export(Enum):
    """Trigger Exporting options"""
    none            = 0
    Source_trig     = 1
    Synced_trig     = 2
    Delayed_trig    = 3

class loglevel(Enum):
    """Same as Python logger module, https://docs.python.org/2/library/logging.html --> 15.7.2 chart"""
    CRITICAL    =   50
    ERROR       =   40
    WARNING     =   30
    INFO        =   20
    DEBUG       =   10
    NOTSET      =   0

class burst_mode(Enum):
    """Signal Generation mode options: burst(ed) or continuous"""
    burst       =   0
    continuous  =   1

class datatypes(Enum):
    """(Waveform) Datatypes that can be sent to/from instrument. Typically used: interleaved_I16"""
    none                =   0
    string              =   1
    interleaved_I16     =   2
    interleaved_I32     =   3
    I16_array           =   4
    I32_array           =   5
    JSONstring          =   6

class Errcode(Enum):
    """Error code that is sent in responses and set by the sender"""
    OK          = 0
    WARN        = 1
    ERROR        = 2
    UNKN        = 3


# =================

# class communication(object):
#     """Communication module
#
#      Abstraction of using whatever channel, e.g pure TCP/IP, ZMQ sub-pub, ZMQ REQ-REP or else..
#
#      Attributes:
#          None: this is the main parent class
#      """
#     sock=""
#
#     def __init__(self):
#         pass
#
# class comm_zmq(communication):
#     """Communication module, ZMQ *
#
#      Abstraction of using whatever channel, e.g pure TCP/IP, ZMQ sub-pub, ZMQ REQ-REP or else..
#
#      Attributes:
#          None: this is the main parent class
#      """
#
#     def __init__(self, host,port,protocol="tcp", pattern="REQREP"):
#         """
#         :param host: IP address or name
#         :param port:
#         :param protocol: tcp / udp
#         :param pattern: REQREP, PUBSUB
#         """
#
#         # https://zeromq.org/languages/python/
#         context = zmq.Context()
#         #  Socket to talk to server
#         print("Connecting to server…")
#         self.sock = context.socket(zmq.REQ)         #Create REQUEST endpoint - Client
#         self.sock.setsockopt(zmq.RCVTIMEO,500)      #set socket option: recieve timeout
#         self.sock.setsockopt(zmq.SNDTIMEO,500)      #set socket option: send timeout
#         socketstring="%s://%s:%s"%(protocol,host, port) # "tcp://localhost:5555"
#         self.sock.connect(socketstring)             #connect to server (LV vi)
#
#     def process_status_multipart(self,status):
#         """
#
#         :param status:
#         :return:
#         """
#         status2 = []
#         try:
#             logger.debug(type(status))
#             print(type(status), len(status))
#             print(status)
#
#             # for i in status:
#             #     i_decoded=i.decode()
#             #     print(type(i_decoded))
#             #     print(str(i_decoded))
#
#             for k in status:
#                 print(status.index(k))
#                 if status.index(k) == 0:
#                     status2.append(str(status[status.index(k)].decode()))
#                 elif status.index(k) == 1:
#                     status2.append(str(status[status.index(k)].decode()))
#                 elif status.index(k) == 2:
#                     status2.append(str(status[status.index(k)].decode()))
#                 elif status.index(k) == 3:
#                     status2.append(str(status[status.index(k)].decode()))
#                 else:
#                     pass
#
#             for i in status2:
#                 print(type(i))
#                 print(i)
#             print(status2)
#             return status2
#         except:
#             info = sys.exc_info()[1]
#             status2.append(str(info))
#             return status2
#
#     def send_float(self,command:str,param: dict, data: float) -> str:
#         """Sending float data
#         :param command:
#         :param param:
#         :param data:
#         :return:
#         """
#         try:
#             typ = "float"
#             typ = str(type(data)).split('\'')[1].split('\'')[0] # float
#             # self.sock.send_string(command)         #send message
#             self.sock.send_string(command, zmq.SNDMORE)  # send message
#             self.sock.send_string(json.dumps(param, indent=2), zmq.SNDMORE)  # send parameters flattened to json
#             # self.sock.send_string(str(data.dtype), zmq.SNDMORE) # send datatype
#             self.sock.send_string(typ, zmq.SNDMORE)  # send datatype
#             self.sock.send_string(str(data))
#             # self.sock.send(data.tobytes())                      # flatten numpy array to bytes and send it
#             #status = self.sock.recv_string()  # retrieve status string
#             status = self.sock.recv_multipart()
#         except:
#             status = sys.exc_info()[1]
#         #print(status)
#         logger.debug(type(status))
#         status2 = self.process_status_multipart(status)
#         return status2
#
#     def send_command(self, command:str, param: dict) -> str:
#         """
#         Sending pure command without any data
#         :param self:
#         :param command:
#         :return:
#         """
#
#         try:
#             typ = "none"
#             data=0
#             #typ = str(type(data)).split('\'')[1].split('\'')[0] # float
#             # self.sock.send_string(command)         #send message
#             self.sock.send_string(command, zmq.SNDMORE)  # send message
#             self.sock.send_string(json.dumps(param, indent=2), zmq.SNDMORE)  # send parameters flattened to json
#             # self.sock.send_string(str(data.dtype), zmq.SNDMORE) # send datatype
#             self.sock.send_string(typ, zmq.SNDMORE)  # send datatype
#             self.sock.send_string(str(data))
#             # self.sock.send(data.tobytes())                      # flatten numpy array to bytes and send it
#             #status = self.sock.recv_string()  # retrieve status string
#             status = self.sock.recv_multipart()
#         except:
#             status = sys.exc_info()[1]
#         #print(status)
#         logger.debug(type(status))
#         status2 = self.process_status_multipart(status)
#         return status2
#
#     def send_waveform(self, command, param, data):
#         """
#         :param param:
#         :param data:
#         :return:
#         """
#         try:
#             typ = "float"
#             typ = str(type(data)).split('\'')[1].split('\'')[0] # float
#             # self.sock.send_string(command)         #send message
#             self.sock.send_string(command, zmq.SNDMORE)  # send message
#             self.sock.send_string(json.dumps(param, indent=2), zmq.SNDMORE)  # send parameters flattened to json
#             # self.sock.send_string(str(data.dtype), zmq.SNDMORE) # send datatype
#             self.sock.send_string(typ, zmq.SNDMORE)  # send datatype
#             #self.sock.send_string(str(data))
#             self.sock.send(data.tobytes())                      # flatten numpy array to bytes and send it
#             #status = self.sock.recv_string()  # retrieve status string
#             status = self.sock.recv_multipart()
#         except:
#             status = sys.exc_info()[1]
#         print(status)
#
#         return status
#         #ToDo: 2020-02-26...finished here...