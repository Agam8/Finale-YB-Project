import sqlite3
import socket
import tcp_by_size

IP = '0.0.0.0'
PORT = 8888
def handle_client_msg(request):
    data = cli_sock.recv()
    req_code = data[4]

def login(cli_sock):
    recv_data = handle_client_msg(request).decode()

def handle_client(cli_sock,i,addr):
    print(f'client #{i} connected from {addr}')
    login(cli_sock)

def main():
    threads = []
    srv_sock = socket.socket()

    # assigning an ip address and port number to a socket instance
    srv_sock.bind((IP,PORT))

    srv_sock.listen(20)
    print('after listen ... start accepting')

    # next line release the port
    srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    i = 1
    while True:
        print('Main thread: before accepting ...')
        cli_sock, addr = srv_sock.accept()
        t = threading.Thread(target=handle_client, args=(cli_sock, str(i), addr))
        t.start()
        i += 1
        threads.append(t)
        if i > 4:  # for tests change it to 4
            print('Main thread: going down for maintenance')
            break

    all_to_die = True
    print('Main thread: waiting to all clients to die')
    for t in threads:
        t.join()
    srv_sock.close()
    print('Bye ..')


if __name__ == '__main__':
    main()
