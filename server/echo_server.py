import socket

from server.data_processing import parse_data, custom_response

def echo_server(download_que):
    HOST, PORT = '0.0.0.0', 4709
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(parse_data(data))
                    download_que.put(parse_data(data))
                    conn.sendall(custom_response)