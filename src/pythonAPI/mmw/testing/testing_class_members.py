"""This script is for testing behavior of list class members"""

class test1():
    lst = list()
    el = ""
    def __init__(self):
        self.lst2 = list()


    def add_new_element(self, element):
        self.lst.append(element)
        self.lst2.append(element)
        #print("elem")
        #self.el = element
        return 0
    def get_lst(self):
        #print (self.lst)
        return self.lst
    def get_lst2(self):
        return self.lst2
    def get_el(self):
        return self.el



def main1():
    t = test1()
    t2 = test1()

    t.add_new_element(1)
    t.add_new_element(2)

    print(t.get_lst())
    print(t2.get_lst())
# Result (t2 and t shares the members):
#[1, 2]
#[1, 2]

    print(t.get_lst2())
    print(t2.get_lst2())

# Result (t2 and t don't share the members defined under __init__ !!):
#[1, 2]
#[]

#main1()
#===================

class test2():
    "Test the same with as in test1, but with dictionaries"
    dct = dict()
    def __init__(self):
        self.dct2 = dict()

    def add_new_element(self, element, dictname):
        self.dct[dictname] = element
        self.dct2[dictname] = element
        return 0
    def get_dct(self):
        #print (self.lst)
        return self.dct
    def get_dct2(self):
        return self.dct2

def main2():
    t = test2()
    t2 = test2()

    t.add_new_element(1,"first")
    t.add_new_element(2,"second")

    print(t.get_dct())
    print(t2.get_dct())
# Result (t2 and t shares the members):
#{'first': 1, 'second': 2}
#{'first': 1, 'second': 2}

    print(t.get_dct2())
    print(t2.get_dct2())

# Result (t2 and t don't share the members defined under __init__ !!):
#{'first': 1, 'second': 2}
#{}

#main2()

# test ZMQ
import zmq

class comm(object):
    context = list()
    sockets = list()
    def __init__(self, host, port, session_name, recv_to = 500, send_to = 500 ):
        socketopts = dict()
        self._create_context()
        self.connect_to_listener(host, port , session_name, recv_to, send_to, "tcp", "REQREP")

    # def connect_to_listener(self, host, port,session_name, recv_to = 500, send_to = 500, protocol="tcp", pattern="REQREP"):
    #     """Connecting to a ZMQ listener (to server)
    #
    #     :param host:
    #     :param port:
    #     :param session_name:
    #     :param recv_to:
    #     :param send_to:
    #     :param protocol:
    #     :param pattern:
    #     :return:
    #     """
    #
    #     self.recv_timeout = recv_to
    #     self.send_timeout = send_to
    #     self.host, self.port = host, port
    #     # https://zeromq.org/languages/python/
    #     logger.debug("RECV_TO: %s, SEND_TO: %d"%(recv_to, send_to))
    #     try:
    #
    #         #  Socket to talk to server
    #         logger.debug("========== Connecting to server %s on port %s …"%(host, port))
    #         self.sock = self.context.socket(zmq.REQ)  # Create REQUEST endpoint - Client
    #         self.sock.setsockopt(zmq.RCVTIMEO, self.recv_timeout)  # set socket option: receive timeout
    #         self.sock.setsockopt(zmq.SNDTIMEO, self.send_timeout)  # set socket option: send timeout
    #         socketstring = "%s://%s:%s" % (protocol, host, port)  # "tcp://localhost:5555"
    #         self.sock.connect(socketstring)  # connect to server (LV vi)
    #         self.sockets.append(sess)
    #         return 0, "OK"
    #     except:
    #         info = sys.exc_info()[1]
    #         return 2, info

    def _create_context(self):
        print(len(self.context))
        if len(self.context) > 1:
            raise Exception("Too many Context: %d"%len(self.context))
        if not self.context:
            print("Create context")
            self.context.append(zmq.Context())
            return 0

def main3():
    host="192.168.40.171"
    c = comm(host,5555,"instrA")
    #c.create_context()
    print(c.context)
    #if c.context: print("exists")
    c2 = comm(host,5558,"ServiceA")
    #c2.create_context()
    print(c2.context)

#main3()

def merge_dictionaries(x,y):
    """https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression-in-python"""
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
print(merge_dictionaries(x,y))