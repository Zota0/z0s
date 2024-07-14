import socket

HOST = '127.0.0.1' # host for reading data
PORT = 32666 # port for reading data
TIMEOUT = 1 # seconds for timeout
BUFFER_SIZE = 4096  # buffer size for reading data

def read_from_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.settimeout(TIMEOUT)

        
        REQUEST = f"GET / HTTP/1.1\r\nHost: localhost:{PORT}\r\n\r\n"
        sock.sendall(REQUEST.encode())

        
        data = b''
        while True:
            chunk = sock.recv(BUFFER_SIZE)
            if not chunk:
                break
            data += chunk

            
            decoded_data = data.decode()
            headers, body = decoded_data.split('\r\n\r\n', 1) 

            return headers, body

headers, body = read_from_port(32666)
