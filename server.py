import mimetypes
import os
import socket

HOST = "0.0.0.0"
PORT = 8000
BASE_DIR = os.path.abspath("html-docs")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket.bind((HOST, PORT))
client_socket.listen(1)

print("LISTENING ON PORT %s" % PORT)


while True:
    client_connection, client_address = client_socket.accept()

    request = client_connection.recv(1024).decode()
    print(f"\n--- Request from {client_address} ---")
    print(request)

    # Parse HTTP request line
    headers = request.split("\n")
    if not headers or len(headers[0].split()) < 2:
        client_connection.close()
        continue

    method, path = headers[0].split()[:2]
    if path == "/":
        path = "/index.html"

    # Sanitize path to prevent directory traversal
    requested_path = os.path.abspath(os.path.join(BASE_DIR, path.lstrip("/")))
    if not requested_path.startswith(BASE_DIR):
        response = "HTTP/1.0 403 FORBIDDEN\n\nAccess denied."
        status_code = 403

    elif not os.path.exists(requested_path) or not os.path.isfile(requested_path):
        response = (
            "HTTP/1.0 404 NOT FOUND\n\nThe requested file was not found on the server."
        )
        status_code = 404

    else:
        with open(requested_path, "rb") as file:
            content = file.read()

        mime_type, _ = mimetypes.guess_type(requested_path)
        mime_type = mime_type or "application/octet-stream"

        response_headers = f"HTTP/1.0 200 OK\nContent-Type: {mime_type}\n\n"
        response = response_headers.encode() + content
        status_code = 200

    # Log result
    print(f"Served: {path} → Status: {status_code}")

    # Send full response
    if isinstance(response, str):
        response = response.encode()
    client_connection.sendall(response)
    client_connection.close()
