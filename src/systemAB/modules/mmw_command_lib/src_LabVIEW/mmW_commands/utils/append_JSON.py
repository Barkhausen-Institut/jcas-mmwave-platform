import numpy as np

def func_append_JSON(json_string:str, new_key:str, new_value:str) -> str:
        """

        :param json_string:
        :param new_key:
        :param new_value:
        :return:
        """
        import json

        appended_JSON = ""

        data = json.loads(json_string)
        data[new_key] = new_value

        appended_JSON = json.dumps(data)

        return appended_JSON



def send_waveform():
        #import zmq
        #import json
        import numpy as np

        # prepare some IQ array
        I = np.array([1, 0, 1, 0])
        Q = np.array([0, -1, 0, -1])

        #data = "default"

        #data = np.empty((I.size + Q.size), dtype=np.float) # np.float64
        #data = np.empty((I.size + Q.size), dtype=int)
        data = [1, 0, 1, 0, 1, 0, 1, 0]
        data[0::2] = I
        data[1::2] = Q

        # self.sock.send_string("tx_iq", zmq.SNDMORE)  # send message
        # self.sock.send(data.tobytes())
        # try:
        #         # response is command status: OK or error
        #         status = self.sock.recv_string()
        #         print(status)
        #
        # except:
        #         print('timeout')
        #data = data.tobytes()
        print(type(data))
        return str(data)

def add(a:int, b:int):
        return a+b

print(send_waveform())