import select
import socket

with socket.socket() as sock:
    sock.bind(('', 10001))
    sock.listen()

    conn1, addr1 = sock.accept()
    conn2, addr2 = sock.accept()

    conn1.setblocking(0)
    conn2.setblocking(0)

    epoll = select.epoll()
    epoll.register(conn1.fileno(), select.EPOLLIN | select.EPOLLOUT)
    epoll.register(conn2.fileno(), select.EPOLLIN | select.EPOLLOUT)

    conn_map = {
        conn1.fileno(): conn1,
        conn2.fileno(): conn2,
    }

    while True:
        events = epoll.poll(1)
        for fileno, event in events:
            if event & select.EPOLLIN:
                data = conn_map[fileno].recv(1024)
                print(data.decode('utf-8'))
            elif event & select.EPOLLOUT:
                conn_map[fileno].send('Посылка'.encode('utf-8'))