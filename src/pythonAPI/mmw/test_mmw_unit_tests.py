"""
Unit tests main script

There a 2 ways running all unit tests:
1. simply run this py file. This way all unit test will run under ths current folder (of this py file) and subfolders.
2. run in command line. First enter to wanted folder and run "pytest -v" command.

"""


import pytest
import os, sys

#@pytest.mark.skip(reason="no way of currently testing this")
def test_convert_to_list():
    """
    Helpers function
    :return:
    """
    from . import mmw_helpers as helpers
    #convert_to_list(data):
    testvector = (
        "test1",
        ("test2", "test3", "test4"),
        ["test5", "test6", "test7"]
    )
    expected_results = (
        ["test1"],
        ["test2", "test3", "test4"],
        ["test5", "test6", "test7"]
    )

    a = "test1"
    b = ("test2", "test3", "test4")
    c = ["test5", "test6", "test7"]
    print("=========================")

    for v in testvector:
        print(v)
        index = testvector.index(v) # get value's index
        result = helpers.generic_helpers.convert_to_list(v)
        print(result)
        assert (type(result) == type(expected_results[index]))
        assert (set(result) == set(expected_results[index]))
    # result = helpers.generic_helpers.convert_to_list(b)
    # print(result)
    # result = helpers.generic_helpers.convert_to_list(c)
    # print(result)
    # >>>
    # <class 'str'>
    # <class 'list'>
    # ['test1']
    # <class 'tuple'>
    # <class 'list'>
    # ['test2', 'test3', 'test4']
    # <class 'list'>
    # <class 'list'>
    # ['test5', 'test6', 'test7']

def main():
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pytestcmd = "cd %s & pytest -v"%current_dir
    results = os.popen(pytestcmd).read()

    print("%s"%results)  # Print results
    return 0                    # return with 0 --> means no error

if __name__ == "__main__":
    #print (sys.argv)
    main()
    sys.exit(0)

