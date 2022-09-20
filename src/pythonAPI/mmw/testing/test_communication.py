"""Unit test for communication module. Use pytest for running it"""

import pathlib
script_dir = pathlib.Path(__file__).parent.resolve()
print(script_dir)
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import communication

def manual_test():
    host = "192.168.40.171"
    c = communication.comm_zmq(host, 5555, "instrB", 500, 500)
    # c.create_context()
    print(c.context)
    print(c.sockets)
    c.send_command("instr:configure_fs", {})

    # if c.context: print("exists")
    c2 = communication.comm_zmq(host, 5558, "serviceB", 500, 500)
    # c2.create_context()
    print(c2.context)
    print(c2.sockets)
    c2.send_command("env:get_instrument_status",{})

manual_test()