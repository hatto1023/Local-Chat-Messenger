import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = './tmp/socket_file'

try:
    sock.connect(server_address)
    print('connected to {}'.format(server_address))
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    user_input =  input('Enter a message: ')
    message = user_input.encode('utf-8')
    sock.sendall(message)

    sock.settimeout(3)

    try:
        while True:
            data = sock.recv(4096)

            if data:
                print('Server response: ' + data.decode('utf-8'))
            else:
                break
    except(TimeoutError):
        print('Socket timeout, ending listening for server messages')

finally:
    print('closing socket')
    sock.close()