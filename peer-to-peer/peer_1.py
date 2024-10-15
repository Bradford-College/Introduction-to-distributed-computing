import socket

def start_peer_1():
    # Set up the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 6000))  # Change port if needed
    server_socket.listen(1)
    print("Peer 1 waiting for connection...")

    # Accept a connection
    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")
    
    # Receive message
    message = conn.recv(1024).decode()
    print(f"Received from Peer 2: {message}")

    # Close the connection
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_peer_1()
