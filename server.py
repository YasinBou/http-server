import socket

HOST = "0.0.0.0"
PORT = 8000

# AF_INET = ipv4 specification.
# SOCK_STREAM = TCP socket specification.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# SOL_SOCKET = socket level indication.
# SO_REUSEADDR = allows the port to be reused without waiting for the os to clear it.
# 1 means "enable this option"
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binds the socket to the ip and port we have set.
client_socket.bind((HOST, PORT))

# Tells the socket to start listening for incoming connections.
# 1 = backlog aka the maximum number of queued connections waiting to be accepted.
client_socket.listen(1)

# Log listening session
print("LISTENING ON PORT %s" % PORT)

# An infinite loop to keep the server running - always ready to accept new client connections.
while True:
    # Await connections.
    client_connection, client_adress = client_socket.accept()

    # .recv(1024) Receives up to 1024 bytes of data from the client.
    # .decode() Converts bytes to a string (assumed UTF-8 by default)
    request = client_connection.recv(1024).decode()

    # Log HTTP request.
    print(request)

    # Response that welcomes the user to our server.
    response = "HTTP/1.0 200 OK\n\nWelcome to my web server!"

    # .encode() converts the response string to bytes.
    # .sendall() sends all the bytes of the response to the client.
    client_connection.sendall(response.encode())

    # Closes the connection when the client is done talking to the server.
    client_connection.close()
