import socket

PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
HOST = "192.168.78.219"  # Standard loopback interface address (localhost)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            print(str(data))
            if not data:
                break
            conn.sendall(data)
