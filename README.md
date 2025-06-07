# Simple Python HTTP Server

A lightweight, custom HTTP server implemented in Python using the `socket` module. This project demonstrates foundational networking concepts, low-level HTTP handling, and secure file serving with MIME type detection.

---

## Overview

This server listens on a configurable port (default 8000) and serves static HTML and other files from a local directory (`html-docs`). It handles HTTP requests by:

- Parsing raw HTTP requests via sockets
- Serving files with correct MIME types
- Preventing directory traversal attacks through path sanitization
- Returning appropriate HTTP status codes (200, 403, 404)
- Logging requests and server activity to the console

This project showcases practical knowledge in:

- Python networking (`socket` programming)
- Basic HTTP protocol mechanics
- Security best practices for serving static content
- File I/O and MIME type handling
- Debugging and logging

---

## Features

- **Custom HTTP request parsing** without using high-level frameworks
- **Secure path handling** to restrict file access within a designated folder
- **Dynamic MIME type detection** for proper content-type headers
- **Console logging** of requests and responses for monitoring

---

## Getting Started

### Prerequisites

- Python 3.x

### Setup

1. Clone this repository
2. Add your static HTML, CSS, JS, or other files inside `html-docs`
3. Run the server:

```bash
python server.py
