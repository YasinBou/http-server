import socket

HOST = "0.0.0.0"
PORT = 8000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket.bind((HOST, PORT))
client_socket.listen(1)

print("LISTENING ON PORT %s" % PORT)

while True:
    # Await connections.
    client_connection, client_adress = client_socket.accept()

    # Log calls.
    request = client_connection.recv(1024).decode()
    print(request)

    response = "HTTP/1.0 200 OK\n\nWelcome to my web server!"
    client_connection.sendall(response.encode())
    client_connection.close()
