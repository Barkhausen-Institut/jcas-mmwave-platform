"""@package mmW_module
mmw.py - mmmWave driver module for NI mmW Test System and its LabVIEW driver

Author(s): NOFFZ Technologies GmbH, Vuk Obradovic and Peter Vago, 2020
"""

global version

version="ver. 2020-05-21"

import sys
import json
import numpy as np

from enum import Enum
from . import communication
from . import mmw_constants as const
from . import mmw_config as conf
from . import mmw_helpers as helpers
import time
from multiprocessing import Queue
from threading import Thread

import logging
# Enable logging of this module: logger=logging.getLogger("mmW"); Disable: logger=logger=logging.getLogger("not_such_logger")
logger=logging.getLogger("mmW")

global perf
perf_ = helpers.performance()

def getversion():
    """Get module version. Prints and Returns version string."""
    print(version)
    pass
    return version

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

def validate_error_code(errcode_string):
    """Validate if error-code is member of commands_enum

    :param errcode_string: error-code_string: command in string type
    :return: Boolean. True if command is valid.
    """
    # ToDO: implement real validation
    #print(const.Errcode._member_names_)
    if errcode_string in const.Errcode._member_names_:
        return True
    else:
        return False

def validate_command_value(command_string):
    """Validate if command is member of commands_enum

    :param command_string: command in string type
    :return: Boolean. True if command is valid.
    """
    # ToDo implement real validation
    return True

def validate_parameters_json(command_str, param_dict):
    """Validate if parameters_json has proper format for the command

    :param command_str: current command on string format
    :param param_dict: parameters dictionary
    :return: Boolean. True if command is valid.
    """
    # ToDO: implement real validation
    return True

def validate_outgoing_message(command_str, param, data=""):
    """Validating outgoing message parameter according to comamnd

    :param command_str:
    :param param:
    :param data:
    :return: True if valid
    """
    valid = True
    if not valid:
        raise Exception("Invalid outgoing message parameters: %s"%(str(param)))
    return True

def process_response_command(r, msg_part1):
    """Processing the first element of multipart message

    :param r: dict
    :param msg_part1: encoded byte stream
    :return: r
    """
    try:
        tmp = msg_part1.decode()
        parts = tmp.split(":")
        if parts[0].strip() != "resp":
            raise Exception("Invalid response format: '%s'"%(str(tmp)))


        r["Errcode"] = parts[1].strip() # b'resp:OK:initialize_hw' OR b'resp:initialize_hw:OK' (2nd is the newer version)
        r["Command"] = parts[2].strip() # b'resp:OK:initialize_hw' OR b'resp:initialize_hw:OK'
        if not validate_error_code(r["Errcode"]):
            # Try it with swapped... this is backward-comaptibility thing
            r["Errcode"] = parts[2].strip()  # b'resp:OK:initialize_hw' OR b'resp:initialize_hw:OK' (2nd is the newer version)
            r["Command"] = parts[1].strip()  # b'resp:OK:initialize_hw' OR b'resp:initialize_hw:OK'
            if not validate_error_code(r["Errcode"]):
                raise Exception("Invalid error code: %s"%r["Errcode"])
        #r["Command"] = parts[1].strip() # b'resp:OK:initialize_hw'
        if not validate_command_value(r["Command"]):
            raise Exception("Invalid command: %s"%r["Command"])
    except:
        raise Exception(sys.exc_info()[1])
        #r["Errcode"]="Invalid response format: '%s' /%s/ "%(str(tmp),sys.exc_info()[1])
    return r # r:

class ni_mmw_parent(object):
    """NI mmW Test System driver
    Attributes:
        None: this is the main parent class
    """
    """modes"""
    modes = const.opmodes.RF
    commlib = "" # commlib # communication session to instrument application
    comm_service = "" # communication session to mmW_service
    instr={"host":"127.0.0.10", "port":"1"} # instrument data, initialize_hw method overwrites its values
    myhost = ""
    myport_instr = conf.default_instrument_port
    myport_service = conf.default_service_port
    timeout_for_receive_data=5000 # ms
    lck = 0

    def _commlib_open(self):
        recv_to_ms = 5000
        send_to_ms = 5000
        session_name = "%s_instr"%(str(self.myhost)) # e.g. 192.168.40.170_instr
        self.commlib = communication.comm_zmq(self.myhost, self.myport_instr, session_name, recv_to_ms, send_to_ms) # Instantiate Comm Library

        self.commenv = str()
        if conf.service_enabled:
            session_name = "%s_service"%(str(self.myhost)) # e.g. 192.168.40.170_instr
            self.commenv = communication.comm_zmq(self.myhost, self.myport_service, session_name, recv_to_ms, send_to_ms) # Instantiate Comm Library


    def _commlib_connect(self, recv_to, send_to):
        """Deprecated: connection is made when calling _commlib_open()"""
        pass
        # status = self.commlib.connect_to_listener(self.myhost, self.myport_instr ,"tcp", "REQREP", recv_to, send_to) # host, port, {"tcp","udp"}, {"REQREP"}, recv_timout 500 (ms), send timeout 500 (ms)
        # if conf.service_enabled:
        #   self.commlib.connect_to_listener(self.myhost, self.myport_instr ,"tcp", "REQREP", recv_to, send_to) # host, port, {"tcp","udp"}, {"REQREP"}, recv_timout 500 (ms), send timeout 500 (ms)


    def _commlib_change_timeouts(self,recv_to, send_to):
        self.commlib.set_socket_timeout(recv_to, send_to)

    def _commenv_change_timeouts(self,recv_to, send_to):
        self.commenv.set_socket_timeout(recv_to, send_to)

    def __init__(self,host,port=conf.default_instrument_port,protocol="tcp"):
        """ Class constructor
        :param host: IP address or domain name of the instrument
        :param port: TCP port
        """
        self.lck = mylock()
        self.instr["host"]=host
        self.myhost = host
        #logger.info("got: %s, set: %s"%(host, self.instr["host"]))
        self.instr["port"]=port
        self.myport_instr = port
        self._commlib_open()
        #self.commlib = communication.comm_zmq() # Instantiate Comm Library
        logger.debug("Comm Lib version: %s"%(str(self.commlib.get_version())))

        #print(version)
        logger.debug(version)

    def _test(self):
        """ Test method

        Args:
            None:
            a (int, optional): DESCRIPTION. Defaults to 10.

        Returns:
            None: DESCRIPTION.

        """
        print("Sending integer")
        test_freq=10
        #self.commlib.set_tx_freq(test_freq)
        print ("Sending sinewave....skipped")

    def _process_response_parameters(self, command, msg_part2):
        """Decodicng Parameters JSON and validating it by the current command

        :param msg_part2: encoded byte stream
        :return: decoded dictionary, Parameters JSON
        """
        param_dict = {} #parameters dictionary, buffer
        logger.debug(msg_part2)
        try:
            params = msg_part2.decode()
            param_dict = json.loads(params)
            # ToDo: Validate parameters based on mmW-specific commands
            if not validate_parameters_json(command, param_dict):
                raise Exception("Invalid parameters for this command('%s'): '%s'"%(str(command), str(param_dict)))
        except:
            raise Exception(sys.exc_info()[1])
        try:
            param_dict["datatype"] = const.datatypes[param_dict["datatype"]] # string ->to Enum
        except:
            logger.error("KeyError: %s, Params: %s"%(sys.exc_info()[1], str(param_dict)))
            param_dict["datatype"] = const.datatypes.none

        return param_dict

    def _process_response_data(self, datafield, datatype = const.datatypes.none):
        """Processing Response Data based on datatype field
            none -> empty string
            string -> string
            JSON string -> string contains valid JSON message
            interleaved_I16 , .._I32: numpy.ndarray numpy.int16

        :param datafield: byte-stream
        :param type: datatype Enum, values are defined in mmy_constants.datatype Enum (class)
        :return: code int, type Enum, data (its datatype is dependent on type field)
        """
        code = 0
        logger.debug("Processing data. Datatype: %s"%str(datatype))
        if datatype in  (const.datatypes.none, const.datatypes.string) :
            data = datafield.decode()
        elif datatype == const.datatypes.JSONstring:
            try:
                data = json.loads(datafield.decode())
            except:
                data = {}
                raise Exception("Unable to unpack JSON data.")
        elif datatype in (const.datatypes.interleaved_I16, const.datatypes.I16_array):
            try:
                data = np.frombuffer(datafield, dtype = np.dtype("int16"))
            except:
                data = ()
                raise Exception("Unable to unpack I16 numpy array")
        elif datatype in (const.datatypes.interleaved_I32 or const.datatypes.I32_array):
            try:
                data = np.frombuffer(datafield, dtype = np.dtype("int32"))
            except:
                data = ()
                raise Exception("Unable to unpack I32 numpy array")
        else:
            data = ""
            raise Exception("Unknown datatype. Type: %s, Value: '%s'"%(str(type(datatype)),str(datatype)))

        return data

    def _process_response(self, message):
        """Processing response. Response consists a 3-element string array. Elements are: "Error_code: command", parameters JSON, data (flatten to string)
        :param message:
        :return: status code, status info, r:Dictionary: Errcode, Command, Parameters , data
        """
        r = {"Errcode":"", "Parameters":{}}             # Default value
        status, info, data = 0, "default", "default"    # Default value

        # Validate if message is a multipart message == list
        #logger.debug("%s, %d, %d"%(type(message),len(message),sys.getsizeof(message)))
        if not (isinstance(message, list) or isinstance(message, tuple)) :
            typ = type(message)
            info = "Received message is not in multipart format. (it's a %s)"%(str(typ))
            #raise Exception(info)
            status = 2
            logger.error("%s, %s, %s" % (info, message[0], message[1]))
            return status, info, r, data
        # Validate if message has exactly 3 elements
        if len(message) != 3:
            info = "Received message has improper number of elements. (it's %d)"%(len(message))
            #raise Exception(info)
            status = 2
            logger.error("%s, [0]: %s, [1]:%s" % (info, message[0], message[1]))
            return status, info, r, data
        logger.debug("%s, %s"%(message[0], message[1]))

        # First part, Errcode: command
        try:
            r = process_response_command(r, message[0]) # part1:  e.g. "b'resp:OK: initialize_hw'"
        except:
            status = 2
            info = sys.exc_info()[1]
            logger.error("Error in processing message: '%s'"%str(message[0]))
            return status, info, r, data

        # Second element: parameters
        try:
            r["Parameters"] = self._process_response_parameters(r["Command"],message[1]) # part2 e.g. : {"datatype":none}
        except:
            status = 2
            info = sys.exc_info()[1]
            logger.error("Error in processing message parameters: '%s'"%str(message[1]))
            return status, info, r, data

        # Third element: Data
        try:
            if r["Parameters"]["datatype"] == const.datatypes.none: pass # just to test if this path exists
        except:
            logger.warning("Field datatype was missing in received message. Set to 'none'.")
            r["Parameters"]["datatype"] = const.datatypes.none

        try:
            data = self._process_response_data(message[2], r["Parameters"]["datatype"]) # r["Parameters"]["datatype"] : Enum
        except:
            status = 2
            info = sys.exc_info()[1]
            logger.error("Error in processing message data field")
            return status, info, r, data

        logger.info("Processed parameters: %s"%str(r))

        return status, info, r, data

    def _send_environment_command(self, command, param, timeout=5000):
        """Send command to Environment Manager , aka mmW Service. Comamnd string will be concatenated with a prefix : "env:"
        :param command:
        :param param:
        :return:
        """
        if not conf.service_enabled:
            #return response, data
            logger.debug("Service port connection is disabled (in mmw_config.py)")
            return {},""
        self.lck.wait_until_is_False()
        self.lck.set()

        logger.debug("==== ENV CMD: %s ===="%str(command))
        code = 0

        recv_to = self.timeout_for_receive_data
        send_to= 5000
        self._commenv_change_timeouts(timeout, timeout)
        #self.commenv_connect(recv_to, send_to)

        #SENDING
        #status = self.commlib.connect_to_listener(self.myhost, self.myport ,"tcp", "REQREP", recv_to, send_to) # host, port, {"tcp","udp"}, {"REQREP"}, recv_timout 500 (ms), send timeout 500 (ms)
        command = "env:%s"%command
        size_data = 0 # There is no sent data

        if "datatype" not in param.keys():
            param["datatype"] = "none"
            logger.warning("Field 'datatype' is missing from parameters dictionary")
        #logger.debug("Sending Command: %s, %s"%(command, str(param)))
        perf_.reset("Sending")
        validate_outgoing_message(command, param, "") # Validating before send.
        status, inf = self.commenv.send_command(command, param)
        perf_.record_diff("Sending","validate_and_sendtime")
        sendtime_ms = perf_.read("Sending","validate_and_sendtime")
        info = "Sending: (%d) Cmd: %s, Info: %s"%(status, command, inf)
        if status == 0:
            logger.debug(info)
        else:
            logger.error(info)
            self.lck.reset()
            raise Exception("Error in sending")


        # RECEIVING
        response, data = {} , ""
        #logger.debug("Receiving response...")

        perf_.reset("Reading")
        status, resp = self.commenv.read_response()
        perf_.record_diff("Reading","Response_time")
        resptime_ms = perf_.read("Reading","Response_time")
        try:
            size_resp = sys.getsizeof(resp[2])
        except:
            size_resp = len(resp)

        if size_resp < 100:
            inf = str(resp)
        else:
            info = "%s...Truncated (full size: %s)"%(str(resp)[0:100],str(size_resp))
        info = "Receiving: (%d) Cmd: %s, Info: %s"%(status, command, inf)
        if status == 0:
            logger.debug(info)
        else:
            logger.error(info)
            self.lck.reset()
            raise Exception("Error in sending command: %s"%str(command))

        #info =  "Instr: %s, Command: %s, RECV_TO/SEND_TO: %s/%d, SND/RCV Time: %.1f/%.1f ms, SND/RCV Datasize: %d/%d Bytes" % (self.myhost,command, recv_to, send_to, sendtime_ms, resptime_ms, size_data, size_resp)

        logger.info("Host: %s, ENVCommand: %s, RECV_TO/SEND_TO: %s/%d, SND/RCV Time: %.1f/%.1f ms, SND/RCV Datasize: %d/%d Bytes" % (self.myhost,command, recv_to, send_to, sendtime_ms, resptime_ms, size_data, size_resp))

        #PROCESSING RESPONSE

        #logger.debug("RESP SIZE %d"%(len(resp)))
        status, inf, response, data = self._process_response(resp)  # dict, tuple
        info = "Processing: (%s) Cmd: %s, Info: %s"%(status,command, inf)
        if status == 0:
            logger.debug(info)
        else:
            logger.error(info)
            self.lck.reset()
            raise Exception("Error in processing response. (%s)"%info)

        #logger.debug("Command: '%s', Status Response: '%s'"%(str(command),str(status)))


        self.lck.reset()
        return response, data

    def _send_instr_command(self, command, param, timeout_ms=5000):
        """Send instrument command. Comamnd string will be concatenated with a prefix : "instr:"
        :param command:
        :param param:
        :return:
        """
        self.lck.wait_until_is_False()
        self.lck.set()

        logger.debug("==== INSTR CMD: %s ===="%str(command))
        code = 0

        recv_to = self.timeout_for_receive_data
        send_to= 5000
        self._commlib_change_timeouts(timeout_ms, timeout_ms)
        self._commlib_connect(recv_to, send_to)

        #SENDING
        #status = self.commlib.connect_to_listener(self.myhost, self.myport ,"tcp", "REQREP", recv_to, send_to) # host, port, {"tcp","udp"}, {"REQREP"}, recv_timout 500 (ms), send timeout 500 (ms)
        command = "instr:%s"%command
        size_data = 0 # There is no sent data

        if "datatype" not in param.keys():
            param["datatype"] = "none"
            #logger.warning("Field 'datatype' is missing from parameters dictionary")
        #logger.debug("Sending Command: %s, %s"%(command, str(param)))
        perf_.reset("Sending")
        validate_outgoing_message(command, param, "") # Validating before send.
        status, inf = self.commlib.send_command(command, param)
        perf_.record_diff("Sending","validate_and_sendtime")
        sendtime_ms = perf_.read("Sending","validate_and_sendtime")
        info = "Sending: (%d) Cmd: %s, Info: %s"%(status, command, inf)
        if status == 0:
            logger.debug(info)
        else:
            logger.error(info)
            self.lck.reset()
            raise Exception("Error in sending")


        # RECEIVING
        response, data = {} , ""
        #logger.debug("Receiving response...")

        perf_.reset("Reading")
        status, resp = self.commlib.read_response()
        perf_.record_diff("Reading","Response_time")
        resptime_ms = perf_.read("Reading","Response_time")
        try:
            size_resp = sys.getsizeof(resp[2])
        except:
            size_resp = len(resp)

        if size_resp < 100:
            inf = str(resp)
        else:
            info = "%s...Truncated (full size: %s)"%(str(resp)[0:100],str(size_resp))
        info = "Receiving: (%d) Cmd: %s, Info: %s"%(status, command, inf)
        if status == 0:
            logger.debug(info)
        else:
            logger.error(info)
            self.lck.reset()
            raise Exception("Error in sending command: %s"%str(command))

        #info =  "Instr: %s, Command: %s, RECV_TO/SEND_TO: %s/%d, SND/RCV Time: %.1f/%.1f ms, SND/RCV Datasize: %d/%d Bytes" % (self.myhost,command, recv_to, send_to, sendtime_ms, resptime_ms, size_data, size_resp)

        logger.info("Host: %s, InstrCommand: %s, RECV_TO/SEND_TO: %s/%d, SND/RCV Time: %.1f/%.1f ms, SND/RCV Datasize: %d/%d Bytes" % (self.myhost,command, recv_to, send_to, sendtime_ms, resptime_ms, size_data, size_resp))

        #PROCESSING RESPONSE

        #logger.debug("RESP SIZE %d"%(len(resp)))
        status, inf, response, data = self._process_response(resp)  # dict, tuple
        info = "Processing: (%s) Cmd: %s, Info: %s"%(status,command, inf)
        if status == 0:
            logger.debug(info)
        else:
            logger.error(info)
            self.lck.reset()
            raise Exception("Error in sending")

        #logger.debug("Command: '%s', Status Response: '%s'"%(str(command),str(status)))


        self.lck.reset()
        return response, data

    def _send_waveform(self, command, param, data, timeout_ms = 5000):
        """Sending Waveform

        :param command:
        :param param:
        :param data:
        :return:
        """
        logger.debug("==== CMD: %s ===="%str(command))
        self.lck.wait_until_is_False()
        self.lck.set()
        code = 0

        recv_to = self.timeout_for_receive_data
        send_to= 5000
        self._commlib_change_timeouts(timeout_ms, timeout_ms)
        self._commlib_connect(recv_to, send_to)

        #SENDING
        #status = self.commlib.connect_to_listener(self.myhost, self.myport ,"tcp", "REQREP", recv_to, send_to) # host, port, {"tcp","udp"}, {"REQREP"}, recv_timout 500 (ms), send timeout 500 (ms)
        command = "instr:%s"%command
        size_data = sys.getsizeof(data)
        if "datatype" not in param.keys(): param["datatype"] = "none"
        #logger.debug("Sending Command: %s, %s"%(command, str(param)))
        perf_.reset("Sending")
        validate_outgoing_message(command, param, "") # Validating before send.
        status = self.commlib.send_waveform(command, param, data)
        perf_.record_diff("Sending","sendtime")
        sendtime_ms = perf_.read("Sending","sendtime")

        # RECEIVING
        response, data = {} , ""
        logger.debug("Receiving response...")

        perf_.reset("Reading")
        status, resp = self.commlib.read_response()
        size_resp = sys.getsizeof(resp)
        perf_.record_diff("Reading","Response_time")
        resptime_ms = perf_.read("Reading","Response_time")

        #logger.info("Instr: %s, Command: %s, RECV_TO: %s, SEND_TO: %d, Send Time: %f ms, Response time: %f ms, Response size: %d Bytes" % (self.myhost,command, recv_to, send_to, sendtime_ms, resptime_ms, size_resp))
        logger.info("Instr: %s, Command: %s, RECV_TO/SEND_TO: %s/%d, SND/RCV Time: %.1f/%.1f ms, SND/RCV Datasize: %d/%d Bytes" % (self.myhost,command, recv_to, send_to, sendtime_ms, resptime_ms, size_data, size_resp))

        status, info , response, data = self._process_response(resp)  # int, dict, tuple
        logger.debug("Response: %s"%(str(response)))

        #logger.debug("Command: '%s', Status Response: '%s'"%(str(command),str(status)))

        if code != 0:
            raise Exception("Error in processing : %s"%(str(code)))
        self.lck.reset()
        return response, data

    def _depr__send_waveform(self, command, param, data):
        """

        :param command:
        :param param:
        :return:
        """
        recv_to=5000
        send_to=5000
        self.commlib_connect(recv_to, send_to)
        #status = self.commlib.connect_to_listener(self.myhost, self.myport ,"tcp", "REQREP", recv_to, send_to) # host, port, {"tcp","udp"}, {"REQREP"}, recv_timout 500 (ms), send timeout 500 (ms)

        command = "instr:%s" % command
        if "datatype" not in param.keys():
            param["datatype"] = "none"

        size_data = sys.getsizeof(data)

        #logger.debug("Sending Waveform: %s, %s"%(command, str(param)))
        start = time.perf_counter()
        status = self.commlib.send_waveform(command, param, data)
        sendtime_ms = (time.perf_counter()-start)*1000

        logger.debug("Receiving response...")

        try:
            start = time.perf_counter()
            response = self.commlib.read_response()
            resptime_ms = (time.perf_counter() - start) * 1000
            response, data = self._process_response(response)
            #logger.debug("Response: %s"%(str(response)))
            logger.info("Instr: %s, Command: %s, RECV_TO: %s, SEND_TO: %d, Send Time: %f ms, Response time: %f ms, Data size: %d Bytes" % (self.myhost,command, recv_to, send_to, sendtime_ms, resptime_ms, size_data))
        except:
            response = {}
            errtext = sys.exc_info()[1]
            response["Error"] = errtext
            return 2, response
        #logger.debug("Command: '%s', Status Response: '%s'"%(str(command),str(status)))
        response="%s (%d)"%(str(response), int(code))
        data = ""
        return code, response, data

    def configure_fs(self, fs=-1, port=const.ports.all):
        """ Configuring instrument Sampling frequency (fs)
        :param port: Enum value, const.ports.{ "rxA", "rxB", "tx"}
        :param fs: Sampling frequency in Hz
        :return: response dictionary (ex. {'Errcode': 'OK', 'Command': 'trigger_burst', 'Parameters': {'generic_info': '', 'datatype': 'none', 'source': '', 'Error': '0'}, 'Data': '', dtype=int16)}
        """
        # Prepare command parameters. command string, param dictionary and ...
        command = "configure_fs"
        param = {"port": port.name, "fs":fs}  # must be string -> hwclass.name # must not be Enum
        # Sending the command a reading response
        response, data= self._send_instr_command(command,param)
        #code, response= self._send_float(command,param, float)
        #code, response= self._send_waveform(command,param, waveform)
        return response, data

    def configure_rf(self, fc=-1, gain=-100, port=const.ports.all):
        """Configure instrument RF parameters.
        :param port: Enum value, const.ports.{ "rxA", "rxB", "tx"}
        :param fc: Carrier Frequency in Hz.
        :param gain:  RF ports gain in double floating.
        :return: dict: (ex. {'Errcode': 'OK', 'Command': 'trigger_burst', 'Parameters': {'generic_info': '', 'datatype': 'none', 'source': '', 'Error': '0'}, 'Data': '', dtype=int16)}
        """

        # Prepare command parameters. command string, param dictionary and ...
        command = "configure_rf"
        param = {"port": port.name, "fc" : fc, "gain" : gain}  # must be string -> hwclass.name # must not be Enum
        # Sending the command a reading response
        response, data = self._send_instr_command(command,param)
        #code, response= self._send_float(command,param, float)
        #code, response= self._send_waveform(command,param, waveform)

        return response

    def configure_trigger(self, port=const.ports.all, delay=0, trigger_source=const.trigger_source.Tclk, PXI_trigger_source=0, Trigger_export=const.trigger_export.none, PXI_trigger_destination=1):
        """Configure instrument trigger settings

        @param port: Enum value, const.ports.{ "rxA", "rxB", "tx"}
        @param delay: Trigger Delay on RX port. int, default 0
        @param trigger_source: Enum value, const.trigger_source.{ "TClk", "PXI_Trig"}
        @param PXI_trigger_source: int, default 0
        @param Trigger_export: Enum value, const.trigger_export.{ "none", "Source", "Synced", "Delayed"}
        @param PXI_trigger_destination: int, default 1
        @return:
        """

        # """Configure instrument trigger settings
        # :param port: Enum value, const.ports.{ "rxA", "rxB", "tx"}
        # :param delay: Trigger Delay on RX port. int, default 0
        # :param trigger_source: Enum value, const.trigger_source.{ "TClk", "PXI_Trig"}
        # :param PXI_trigger_source: int, default 0
        # :param Trigger_export: Enum value, const.trigger_export.{ "none", "Source", "Synced", "Delayed"}
        # :param PXI_trigger_destination: int, default 1
        # :return:
        # """
        # Prepare command parameters. command string, param dictionary and ...
        command = "configure_trigger"
        param = {"port": port.name, "delay" : delay , "trigger_source" : trigger_source.name, "PXI_trigger_source" : PXI_trigger_source,
                "Trigger_export" : Trigger_export, "PXI_trigger_destination" : PXI_trigger_destination}  # must be string -> hwclass.name # must not be Enum
        # Sending the command a reading response
        response, data = self._send_instr_command(command,param)
        #code, response= self._send_float(command,param, float)
        #code, response= self._send_waveform(command,param, waveform)
        return response

    def _depr_configure_rx_sync(self, lo1_sh=const.lo1_sharing.Disabled, lo2_sh=const.lo2_sharing.Disabled):
        """Deprecated: Configure RX Synchronization -> lo_sync_enable, trigger_sync_enable
        :param LO1_sharing_enum:
        :param LO2:
        :param sharing_enum:
        :return:
        """

        # # Prepare command parameters. command string, param dictionary and ...
        # command = "initialize_hw"
        # param = {"hwclass": hwclass.name}  # must be string -> hwclass.name # must not be Enum
        #
        # # Sending the command a reading response
        # code, response= self._send_instr_command(command,param)
        # #code, response= self._send_float(command,param, float)
        # #code, response= self._send_waveform(command,param, waveform)
        #
        # return response

        command = "configure_rx_sync"
        param = {"LO1_sharing_value": lo1_sh.value, "LO2_sharing_value": lo2_sh.value, "LO1_sharing_text": lo1_sh.name, "LO2_sharing_text": lo2_sh.name}
        logger.debug("LO Sharing options: %s, %s"%(lo1_sh, lo2_sh))
        logger.debug(str(param))
        # data=[]
        # data.append(freq)
        # print(type(data))
        data = 0.0
        status = self.commlib.send_float(command, param, data)

        return status, "Not implemented"

    def equalization_enable(self, eq_enable = True):
        """Enable/disable wide-band equalization. (Amplitude and phase "flatness" of RF ports)
        :param eq_enable: Boolean {True, False}
        :return:  response dictionary
        """
        # Prepare command parameters. command string, param dictionary and ...
        command = "equalization_enable"
        param = {"Enable": eq_enable}  # must be string -> hwclass.name # must not be Enum
        # Sending the command a reading response
        response, data = self._send_instr_command(command,param)
        #code, response= self._send_float(command,param, float)
        #code, response= self._send_waveform(command,param, waveform)

        return response

    def equalization_start(self):
        """Starts equalization calibration procedure. SysA starts generating calibration signal.
        :return:  response dictionary
        """
        # Prepare command parameters. command string, param dictionary and ...
        command = "equalization_start"
        param = {"no_param": ""}  # must be string -> hwclass.name # must not be Enum
        # Sending the command a reading response
        response, data = self._send_instr_command(command,param)
        #code, response= self._send_float(command,param, float)
        #code, response= self._send_waveform(command,param, waveform)

        return response

    def equalization_stop(self):
        """Stops equlization calibration procedure.
        :return:  response dictionary
        """
        # Prepare command parameters. command string, param dictionary and ...
        command = "equalization_stop"
        param = {"no_param": ""}  # must be string -> hwclass.name # must not be Enum
        # Sending the command a reading response
        response, data = self._send_instr_command(command,param)
        #code, response= self._send_float(command,param, float)
        #code, response= self._send_waveform(command,param, waveform)

        return response

    def fetch(self,timeout=5000):
        """Fetching waveforms from Intrument
        :param timeout: Timeout in ms. Waveform transfer over the network can take longer time. By specifying a longer timeout value it can prevent this method from timing out.
        :return:
        """
        # Prepare command parameters. command string, param dictionary and ...
        command = "fetch"
        param = {"no_param" : ""}
        # Sending the command a reading response
        response, data = self._send_instr_command(command,param, timeout) # timeout will be increased. This is set at start() function
        try:
          if response["Parameters"]["datatype"] == const.datatypes.none:
              data = ""
            #raise Exception("Empty Data")
            #return {}, ""
        except:
            raise Exception("Timeout.")
            return {}, ""
        return response, data

    def get_config(self):
        """Read instrument current configuration parameters
        :return:  response dictionary with status information
        """
       # Prepare command parameters. command string, param dictionary and ...
        command = "get_config"
        param = {"verbosity_level": "4"}  # verbosity (optional): 0....4, 4 is the most verbose
        # Sending the command a reading response
        response, data = self._send_instr_command(command,param)
        #code, response= self._send_float(command,param, float)
        #code, response= self._send_waveform(command,param, waveform)

        #ToDO: convert param field to Py dictionary
        #ToDo: Scientific numbers! Causes Syntax error
        # example = {
        #     "sistem info": {
        #         "mmw instr": "niMmWave_Transciever",
        #         "max fs": 3.07200000000000E+9,
        #         "RX/LO1 src": "External",
        #         "TX/LO1 src": "Internal",
        #         "LO2 src": "Internal",
        #         "RX LO1 export": true,
        #         "TX LO1 export": true,
        #         "LO2 export": true,
        #         "TX LO1 export level": 15.0000000000000,
        #         "RX LO1 export level": 15.0000000000000,
        #         "LO2 export level": 13.0000000000000
        #     },
        #     "state": {
        #         "hw state": 1,
        #         "lo sync en": true,
        #         "trig sync en": true,
        #         "mode": 0
        #     },
        #     "tx": {
        #         "fc": 7.50000000000000E+10,
        #         "gain": -10.0000000000000,
        #         "fs": 3.07200000000000E+9,
        #         "trigger delay": 0.00000000000000
        #     },
        #     "rx": {
        #         "fc": 7.50000000000000E+10,
        #         "gain": 25.0000000000000,
        #         "fs": 3.07200000000000E+9,
        #         "trigger delay": 8.17.000000000000E-9
        #     }
        # }

        # "hw state" is enum:
        # 0: Off
        # 1: Configuration
        # 2: Running
        # 3: Calibration
        #
        # "mode" is enum:
        # 0: RF
        # 1: IF
        # 2: BB

        return response

    def get_instrument_status(self):
        """Read instrument current configuration parameters
        :return:  response dictionary with status information
        """
       # Prepare command parameters. command string, param dictionary and ...
        command = "get_instrument_status"
        param = {"no_param": ""}  # verbosity (optional): 0....4, 4 is the most verbose
        # Sending the command a reading response
        response, data = self._send_environment_command(command,param)
        return response

    def initialize_hw(self, mode = const.opmodes.IF, timeout=60000):
        """Initializes the connection to instrument and sends initialize_hw command to instrument.
        :param mode: Operational modes: Baseband, IF or RF. const.opmodes.{BB,IF,RF}
        :param timout: Re/initilaization takes time. Sometimes takes 45 seconds or more. Especially when op.mode change is requested e.g between RF an IF modes. Default value is 60000 ms.
        :return: response dictionary
        """
        # Prepare command parameters. command string, param dictionary and ...
        command = "initialize_hw"
        param = {"mode":mode.name}  # must be string -> hwclass.name # must not be Enum

        # Sending the command a reading response
        response, data = self._send_instr_command(command,param, timeout)
        #code, response= self._send_float(command,param, float)
        #code, response= self._send_waveform(command,param, waveform)

        return response

    def _depr_initialize_hw(self,hwclass=const.instr_hwclass.Simulated, mode = const.opmodes.IF, timeout_ms=60000):
        """Initializes the connection to instrument and sends initialize_hw command to instrument.
        :param hwclass: Hardware class. Enables using simulated hardware. Enum value const.instr_hwclass.{"Simulated","NI_mmW01","Other"}
        :param mode: Operational modes: Baseband, IF or RF. const.opmodes.{BB,IF,RF}
        :param timout: Re/initilaization takes time. Sometimes takes 45 seconds or more. Especially when op.mode change is requested e.g between RF an IF modes. Default value is 60000 ms.
        :return: response dictionary
        """
        # Prepare command parameters. command string, param dictionary and ...
        command = "initialize_hw"
        param = {"hwclass": hwclass.name, "mode":mode.name}  # must be string -> hwclass.name # must not be Enum

        # Sending the command a reading response
        response, data = self._send_instr_command(command,param, timeout_ms)
        #code, response= self._send_float(command,param, float)
        #code, response= self._send_waveform(command,param, waveform)

        return response

    def enable_LO_sync(self, LO_sync_enable=True):
        """Enable/disable wide-band equalization
        :param LO_sync_enable: Boolean.
        :return: response dictionary
        """
        # Prepare command parameters. command string, param dictionary and ...
        command = "lo_sync_enable"
        param = {"Enable": LO_sync_enable}  # must be string -> hwclass.name # must not be Enum
        # Sending the command a reading response
        response, data = self._send_instr_command(command,param)
        #code, response= self._send_float(command,param, float)
        #code, response= self._send_waveform(command,param, waveform)

        return response

    def reset_hw(self):
        """Sending a Soft-reset to Instrument software and mmW hardware.

        :return: response
        """

        self.timeout_for_receive_data=timeout
        # Convert bursts to array if it was string
        bursts = helpers.generic_helpers.convert_to_list(bursts)

        # Prepare command parameters. command string, param dictionary and ...
        command = "reset_hw"
        param = {"no_param": ""} # Construct a dictionary

        #logger.debug("Command: %s, Parameters: %s"%(command, str(param)))

        # Sending the command a reading response
        response, data = self._send_instr_command(command,param)
        #code, response= self._send_float(command,param, float)
        #code, response= self._send_waveform(command,param, waveform)

        return response

    def set_log_level(self, loglevel = const.loglevel.ERROR):
        """Setting loglevel on instrument side. (for debugging for example)
        :param loglevel: Enum or string. Enum: {CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET}, same as Python logger module: https://docs.python.org/2/library/logging.html
        :return: response dictionary
        """
        # Prepare command parameters. command string, param dictionary and ...
        command = "set_log_level"
        param = {"loglevel_name": loglevel.name, "loglevel_value": loglevel.value}  # must be string -> hwclass.name # must not be Enum
        # Sending the command a reading response
        response, data = self._send_instr_command(command,param)
        #code, response= self._send_float(command,param, float)
        #code, response= self._send_waveform(command,param, waveform)

        return response

    def send_trigger(self, burstmode=const.burst_mode.burst):
        """Sending trigger to master system.

        :param burstmode:
        :return:
        """
        # Prepare command parameters. command string, param dictionary and ...
        command = "send_trigger"
        param = {"burst_mode" : burstmode.name} # must be string -> hwclass.name # must not be Enum
        # Sending the command a reading response
        response, data = self._send_instr_command(command,param) #
        return response

    def shutdown(self):
        """Closes instrument application.
        :return: response dictionary
        """
        # Prepare command parameters. command string, param dictionary and ...
        command = "Shutdown"
        param = {"no_param": ""}  # must be string -> hwclass.name # must not be Enum

        # Sending the command a reading response
        response, data = self._send_instr_command(command,param)
        #code, response= self._send_float(command,param, float)
        #code, response= self._send_waveform(command,param, waveform)

        return response

    def start(self, bursts, acq_length_sec = 400e-6, timeout_ms=15000):
        """Start burst generation.
        :param bursts: 1 or more burst-names. Can be string (1 burst) or array of strings /list/ (multiple bursts)
        :param acq_length: Acquisition length in seconds (float). Default is 10e-6 s (10us). Timeout may need to be increased for longer bursts!
        :param timeout: Timout for receiving waveform over the network (e.g 12s needed for 800us burst). Default is 5000ms.
        :return: response dictionary
        """

        self.timeout_for_receive_data=timeout_ms
        # Convert bursts to array if it was string
        bursts = helpers.generic_helpers.convert_to_list(bursts)

        # Prepare command parameters. command string, param dictionary and ...
        command = "start"
        param = {"acq_length": acq_length_sec, "bursts": bursts} # Construct a dictionary

        #logger.debug("Command: %s, Parameters: %s"%(command, str(param)))

        # Sending the command a reading response
        response, data = self._send_instr_command(command,param, timeout_ms)
        #code, response= self._send_float(command,param, float)
        #code, response= self._send_waveform(command,param, waveform)

        return response

    def stop(self):
        """Stop burst generation
        :return: response dictionary
        """
        # Prepare command parameters. command string, param dictionary and ...
        command = "stop"
        param = {"no_param": ""}  # must be string -> hwclass.name # must not be Enum

        # Sending the command a reading response
        response, data = self._send_instr_command(command,param)
        #code, response= self._send_float(command,param, float)
        #code, response= self._send_waveform(command,param, waveform)

        return response

    def transceive(self, data, burstname="iqdata", acq_length=10e-6, burstmode=const.burst_mode.burst, timeout_ms=2000):
        """Transceive combines write_tx, start, trigger_burst, stop command into a single command.
        :param data: Waveform to send to instrument
        :param acq_length: Acquisition length in seconds (float). Default is 10e-6 s (10us).
        :param burstmode: burst or continuous
        :return: response dictionary
        """

        self.timeout_for_receive_data=timeout
        # Convert bursts to array if it was string
        bursts = helpers.generic_helpers.convert_to_list(burstname)

        # Prepare command parameters. command string, param dictionary and ...
        command = "transceive"
        param = {"burstname":burstname, "acq_length" : acq_length, "bursts": bursts, "burst_mode" : burstmode.name,  "datatype":const.datatypes.interleaved_I16.name} # must be string -> hwclass.name # must not be Enum

        # Sending the command a reading response
        response, data = self._send_waveform(command, param, data, timeout_ms)

        return response, data

    def _depr_trigger_burst(self, bursts, burstmode = const.burst_mode.burst):
        """Retriggers a burst that is already downloaded to instrument.
           Deprecated on 24/04/2020. -> Use send_trigger and fetch methods.
        :param bursts: name of a downlaoded burst (string) or a list of downloaded bursts. Accepts string, list or tuple.
        :param burstmode: burst or continuous
        :return: response dictionary
        """
        # Prepare command parameters. command string, param dictionary and ...
        command = "trigger_burst"
        burstnames = helpers.generic_helpers.convert_to_list(bursts) # any to list
        param = {"bursts" : burstnames, "burstmode" : str(burstmode.name)} # must be string -> hwclass.name # must not be Enum

        # Sending the command a reading response
        response, data = self._send_instr_command(command,param, self.timeout_for_receive_data) # timeout will be increased. This is set at start() function
        #code, response= self._send_float(command,param, float)
        #code, response= self._send_waveform(command,param, waveform)

        return response, data

    def trigger_sync_enable(self, trigger_sync_enable = True):
        """Enables or disables trigger sharing between systems.
        :param trigger_sync_enable:
        :return: response dictionary
        """
        # Prepare command parameters. command string, param dictionary and ...
        command = "trigger_sync_enable"
        param = {"Enable": trigger_sync_enable}  # must be string -> hwclass.name # must not be Enum

        # Sending the command a reading response
        response, data = self._send_instr_command(command,param)
        #code, response= self._send_float(command,param, float)
        #code, response= self._send_waveform(command,param, waveform)

        return response

    def write_tx(self, burstname, data, attribs={}):
        """Downloads waveform to instrument
        :param burst_name:
        :param data:
        :param attribs: dict of datatype=const.datatypes.interleaved_IQ, t0, dt
        :return:
        """
        # Prepare data: validate data type passed to this function. Convert is necessary.

        # Prepare command parameters. command string, param dictionary and ...
        #command = "enable_LO_sync"
        command = "Write TX"
        #ToDo: ensure all elements available in attribs dict
        #ToDO: DBL input data
        #attribs = {"datatype": const.datatypes.interleaved_IQ, "t0": 0, dt: "0.1", "type": attribs["type"], "dtype": attribs["dtype"], "length": attribs["length"]}
        p = {"burstname": str(burstname), "burst_length" : len(data), "datatype":const.datatypes.interleaved_I16.name}  # must be string -> hwclass.name # must not be Enum
        param = {**p, **attribs} # merging 2 dicts, https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression
        #param = p.copy().update(attribs) x This merging is nor working by some reason
        logger.debug("Write_tx Parameters: %s"%str(param))
        # Sending the command a reading response
        #code, response= self._send_instr_command(command,param)
        #code, response= self._send_float(command,param, float)
        # ToDo: possibe data conversion comes here.

        response, data = self._send_waveform(command, param, data)

        return response

    def _depr_set_tx_freq(self,freq):
        """Setting instrument TX Frequency
        :param freq: float
        :return:
        """
        # Prepare command parameters. command string, param dictionary and ...
        command = "initialize_hw"
        param = {"hwclass": hwclass.name}  # must be string -> hwclass.name # must not be Enum

        # Sending the command a reading response
        code, response= self._send_instr_command(command,param)
        #code, response= self._send_float(command,param, float)
        #code, response= self._send_waveform(command,param, waveform)

        return response

        command="set_tx_freq"
        param = {"unit": "Hz"}  # Hz,k,M,G #
        #data=[]
        #data.append(freq)
        #print(type(data))
        data = float(freq)
        response, data = self.commlib.send_float(command, param, data)
        return 0, status

    def _depr_store_waveform(self, name, fs, data):  # Waveform_name:str, Fs[Hz]: float, samples:numpy.ndarray
        """Send waveform to instrument
        :param fs:
        :param wfm:
        :return:
        """
        # Prepare command parameters. command string, param dictionary and ...
        command = "initialize_hw"
        param = {"hwclass": hwclass.name}  # must be string -> hwclass.name # must not be Enum

        # Sending the command a reading response
        code, response= self._send_instr_command(command,param)
        #code, response= self._send_float(command,param, float)
        #code, response= self._send_waveform(command,param, waveform)

        return response
        command = "store_waveform"
        param = {"Wfm_name":name,"Fs":fs}
        status = self.commlib.send_waveform(command, param, data)
        return 0,status

    def _list_commands(self):
        """List all available commands.
        """
        #Todo : implementation is missing
        commands="Todo: writing this function"
        print(commands)

class ni_mmw(ni_mmw_parent):
    """mod: keepeing commlib session connection open
    """
    # def _commlib_open(self):
    #     recv_to = 5000
    #     send_to = 5000
    #     self.commlib = communication.comm_zmq() # Instantiate Comm Library
    #     self.commlib.connect_to_listener(self.myhost, self.myport_instr ,"tcp", "REQREP", recv_to, send_to) # host, port, {"tcp","udp"}, {"REQREP"}, recv_timout 500 (ms), send timeout 500 (ms)

    def _commlib_connect(self, recv_to, send_to):
        # It is connected already..
        pass

# === Multi-threaded fucntions

class ni_mmw_multi(ni_mmw):
    """This is the multithreaded extension of the ni_mmw class
    """


def configure_fs_multi(instr=None):
        """Multi-threaded call of configure_fs method.

        :param instr: list of tuples. Tuple: (instr_session, fs float, port Enum)
        :return: list of responses. Response is the responses of each functions.
        """
        if instr is None:
            instr = [(self.a, 0.1, const.ports.rx)]
        queues = list()
        responses = list()
        threads_list = list()
        for i in instr:
            session, fc, port = i[0], i[1], i[2]
            #print(session, fc, port)
            que = Queue()
            queues.append(que)
            t = Thread(target=lambda q, arg1, arg2: q.put(session.configure_fs(arg1, arg2)), args=(que, fc, port))
            t.start()
            threads_list.append(t)

        # Join all the threads
        for t in threads_list:
            t.join()

        # Check thread's return value
        z = 0
        #print(len(queues))
        for que in queues:
            result = ""
            while not que.empty():
                result = que.get()
                #print(result)
            responses.append(result)
            z+=1

        return responses

def start_multi(instr=None):
        """Multi-threaded call of start method.

        :param self:
        :param instr: ex. [(iA,[wfmname], length, 5000), (iB, [wfmname], length, 5000)]
        :return:
        """
        if instr is None:
            instr = [(self.a, [""], 0.1, 5000)]
        queues = list()
        responses = list()
        threads_list = list()
        for i in instr:
            session, wfmname, length, timout = i[0], i[1], i[2], i[3]
            #print(session, fc, port)
            que = Queue()
            queues.append(que)
            t = Thread(target=lambda q, arg1, arg2, arg3: q.put(session.start(arg1, arg2, arg3)), args=(que, wfmname, length, timout))
            t.start()
            threads_list.append(t)

        # Join all the threads
        for t in threads_list:
            t.join()

        # Check thread's return value
        z = 0
        #print(len(queues))
        for que in queues:
            result = ""
            while not que.empty():
                result = que.get()
                #print(result)
            responses.append(result)
            z+=1

        return responses

def fetch_multi(instr=None):
    """Multi-threaded call of fetch method.

    :param self:
    :param instr: ex. [(iA,5000),(iB,5000)]
    :return:
    """
    if instr is None:
        instr = [self.a]
    myqueues = list()
    responses = list()
    data_list= list()
    threads_list = list()
    for i in instr:
        session, timeout = i[0], i[1]
        # print(session, fc, port)
        que = Queue()
        myqueues.append(que)
        t = Thread(target=lambda q, arg1: q.put(session.fetch(arg1)),args=(que, timeout))
        t.start()
        threads_list.append(t)

    # Join all the threads
    for t in threads_list:
        t.join()

    # Check thread's return value
    z = 0
    # ToDo: process data propely
    #print(len(myqueues))
    for que in myqueues:
        result = ""
        while not que.empty():
            result = que.get()
            # print(result)
            try:
                status = result[0]
                if status == 0:
                    #info = result[1]
                    responses.append(result[2])
                    data_list.append(result[3])
                else:
                    logger.debug(result[0], result[1])
                    responses.append({})
                    data_list.append("")
            except:
                pass
        z += 1
    data = ""
    return responses, data_list

def transceive_multi(instr_session_list,data, burst_name="wfmname", acq_length=10e-6, burst_mode=const.burst_mode.burst, timeout=5000):
    """

    :param instr_session_list:
    :param data:
    :param burst_name:
    :param acq_length:
    :param burst_mode:
    :param timeout:
    :return:
    """
    if instr_session_list is None:
        instr = [self.a]
    myqueues = list()
    responses = list()
    data_list= list()
    threads_list = list()

    for i in instr_session_list:
        session= i
        # print(session, fc, port)
        que = Queue()
        myqueues.append(que)
        # r, data = mmw.transceive_multi([iA, iB], waveform, wfmname, length, mmw.const.burst_mode.burst, 5000)
        t = Thread(target=lambda q, arg1, arg2, arg3, arg4, arg5: q.put(session.transceive(arg1, arg2, arg3, arg4, arg5)), args=(que, data, burst_name, acq_length, burst_mode, timeout))
        t.start()
        threads_list.append(t)

    # Join all the threads
    for t in threads_list:
        t.join()

    # Check thread's return value
    z = 0
    # ToDo: process data propely
    # print(len(myqueues))
    for que in myqueues:
        result = ""
        while not que.empty():
            result = que.get()
            # print(result)
            responses.append(result[0])
            data_list.append(result[1])
            # try:
            #     status = result[0]
            #     if status == 0:
            #         # info = result[1]
            #         responses.append(result[2])
            #         data_list.append(result[3])
            #     else:
            #         logger.error("%s, %s"%(str(result[0]), str(result[1])))
            #         responses.append({})
            #         data_list.append("")
            # except:
            #     pass
        z += 1
    data = ""
    return responses, data_list















