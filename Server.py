import socket
import os

PORT = 2300
HOST = '127.0.0.1'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server is Listening...")
    conn, addr = s.accept()
    print('Got Connection From', addr)

    while True:
        msg_type = conn.recv(1024).decode('utf-8')

        if msg_type == 'upload':
            file_name = conn.recv(1024).decode('utf-8')
            print('Client Sent: ' + file_name)
            file_name = 'server-' + file_name
            data_size = int(conn.recv(1024).decode('utf-8'))
            data = conn.recv(data_size)
            with open(file_name, 'wb') as f:
                f.write(data)

        elif msg_type == 'exec':
            text_message = conn.recv(1024).decode('utf-8')
            print(text_message)
            os.system(text_message)

        elif msg_type == 'send -e':
            pass

        elif msg_type == 'send':
            text_message = conn.recv(1024).decode('utf-8')
            print(text_message)
            print('Client: ' + text_message)

