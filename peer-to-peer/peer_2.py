import socket

def start_peer_2():
    # Set up the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Attempt to connect to Peer 1
    try:
        client_socket.connect(('localhost', 7000))  # Same IP, different port for peer 1
        message = "Hello from Peer 2!"
        client_socket.sendall(message.encode())
        print(f"Sent to Peer 1: {message}")
    except ConnectionRefusedError:
        print("Connection failed. Make sure Peer 1 is running.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_peer_2()
