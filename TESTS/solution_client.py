import socket
import time


class ClientError(Exception):
    pass


class Client:
    ANSWER_STATUS = ('ok', 'error')

    def __init__(self, addr, port, timeout=None):
        self.socket = socket.create_connection((addr, port), timeout=timeout)

    def __del__(self):
        self.socket.close()

    def _data_exchange(self, *args):
        send_data = (' '.join(map(str, args)) + '\n').encode('utf-8')
        try:
            self.socket.send(send_data)
            recive_string = self.socket.recv(1024).decode()
            recive_data = list(recive_string.split('\n'))
            if recive_data[0] in self.ANSWER_STATUS and ''.join(recive_data[-2:-1]) == '':
                return recive_data[1:-2], recive_string
            else:
                raise ClientError
        except ConnectionError:
            raise ClientError

    def get(self, key):
        data, _ = self._data_exchange('get', key)
        result = {}
        for item in data:
            item = tuple(item.split())
            if len(item) != 3:
                raise ClientError
            list_values = [(int(item[2]), float(item[1]))]
            if item[0] in result.keys():
                list_values.extend(result[item[0]])
                list_values.sort()
            result[item[0]] = list_values
        return result

    def put(self, name_metric, value, timestamp=None):
        if self._data_exchange('put', name_metric, value, timestamp or int(time.time()))[1] != 'ok\n\n':
            raise ClientError
