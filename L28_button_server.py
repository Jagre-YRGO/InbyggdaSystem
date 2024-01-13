import socket

PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
HOST = "192.168.0.89"  # Standard loopback interface address (localhost)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
s.bind((HOST, PORT))
s.listen()

while True:
    try:
        conn, addr = s.accept()
    except TimeoutError:
        print('Timed out')
        break
    print(f"Connected by {addr}")
    data = conn.recv(1024)
    print(data.decode("ASCII"))
