import socket

with socket.create_connection(('127.0.0.1', 10001), 5) as sock:
    sock.settimeout(2)
    try:
        sock.sendall('Пакет данных'.encode('utf-8'))
    except socket.timeout:
        print('Таймаут пересылки данных')
    except socket.error as ex:
        print('Ошибка пересылки данных:', ex)
