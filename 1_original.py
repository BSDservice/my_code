import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5050))
server_socket.listen()

while True:
    request_socket, addr = server_socket.accept()
    print(f'подключился {addr}')
    while r := request_socket.recv(4096):
        print(f'request: {r.decode("utf_8")}')
        request_socket.send('answer: получи!\n'.encode())
    else:
        request_socket.close()
        print(f'{addr} отвалился!')
