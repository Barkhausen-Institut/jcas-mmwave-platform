"""Unit test for communication module. Use pytest for running it"""

import pathlib
script_dir = pathlib.Path(__file__).parent.resolve()
print(script_dir)
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest

import communication
from mmw import mmw

def test_validate_error_code():
    #print(mmw.getversion())
    #print(mmw._validate_error_code("OK"))
    assert (mmw.validate_error_code("OK") == True)
    assert (mmw.validate_error_code("ERROR") == True)
    assert (mmw.validate_error_code("WARN") == True)
    assert (mmw.validate_error_code("UNKN") == True)
    assert (mmw.validate_error_code("get_instr_status") == False)

def test_process_response_command():
    r=dict()
    proper = ["resp:start:OK","resp:stop:ERROR","resp:WARN:configure_fs"]
    improper = ["env:start:OK"]
    r_lst = []
    # Positive tests
    for p in proper:
        r = mmw.process_response_command(r, p.encode())
        assert (isinstance(r,dict))

    # Negative tests with pytest.raise
    for p in improper:
        #r = mmw.process_response_command(r, p.encode())
        with pytest.raises(Exception):
            r = mmw.process_response_command(r, p.encode())


test_validate_error_code()
test_process_response_command()
