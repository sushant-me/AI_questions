"""
Create simple chat application.
"""

import socket

def create_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server is listening on port 12345")
    return server_socket

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Received message: {message}")
        client_socket.send("Message received".encode('utf-8'))
    client_socket.close()

def main():
    server_socket = create_server()
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connected by {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    main()