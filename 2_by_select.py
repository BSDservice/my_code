import socket
from select import select


ready_to_read = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5050))
server_socket.listen()


def accept_con(s_sock):

    request_socket, addr = s_sock.accept()
    print(f"УСТАНОВЛЕНО СОЕДИНЕНИЕ С {addr}")
    return (request_socket, addr)


def recive_data(sock):

    if r := sock.recv(4096):

        print(r.decode('utf-8'))
    else:

        print("клиент отвалился")
        ready_to_read.remove(sock)


def event_loop():

    while True:

        sockets_to_read, _, _ = select(ready_to_read, [], [])

        for sock in sockets_to_read:

            if sock is server_socket:

                request_socket, addr = accept_con(sock)
                ready_to_read.append(request_socket)

            else:

                recive_data(sock)



if __name__ == '__main__':

    ready_to_read.append(server_socket)
    event_loop()