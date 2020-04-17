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

    # Метод для обмена данными с сервером. Возвращает список с ответом сервера.
    def _data_exchange(self, *args):
        send_data = (' '.join(map(str, args)) + '\n').encode('utf-8')
        try:
            self.socket.send(send_data)
            resive_string = self.socket.recv(1024).decode()
            recive_data = list(
                map(
                    lambda x: x.split(),
                    resive_string.split('\n')
                )
            )
            if recive_data[0][0] not in self.ANSWER_STATUS:
                raise ClientError
            return recive_data, resive_string
        except ConnectionError:
            raise ClientError

    def get(self, key):
        data, _ = self._data_exchange('get', key)
        result = {}
        if data[0][0] == 'ok':
            try:
                for it in range(1, len(data)):
                    if len(data[it]) == 3:
                        list_values = [(int(data[it][2]), float(data[it][1]))]
                        if data[it][0] in result.keys():
                            list_values.extend(result[data[it][0]])
                            list_values.sort(reverse=True)
                        result[data[it][0]] = list_values
            except ValueError:
                raise ClientError
        return result

    def put(self, name_metric, value, timestamp=None):
        if self._data_exchange('put', name_metric, value, timestamp or int(time.time()))[1] != 'ok\n\n':
            raise ClientError


client = Client('127.0.0.1', 8888, 10)
print(client.get('*'))
