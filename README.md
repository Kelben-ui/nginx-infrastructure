# nginx-infrastructure

Three-day infrastructure lab covering Nginx reverse proxying, load balancing, TLS termination, and monitoring.

## Day 1 — Nginx Reverse Proxy

### Architecture

The client sends HTTP requests to Nginx on port 80.

```text
Client
   |
   | HTTP :80
   v
Nginx Reverse Proxy
   |
   | HTTP :5000
   v
Flask Backend
127.0.0.1:5000
```

The Flask backend listens only on `127.0.0.1:5000`, so it is not directly accessible from the network. Nginx is the network-facing entry point.

### Backend

The backend is implemented using Flask and runs on:

```text
127.0.0.1:5000
```

The backend logs the client IP, original Host header, and forwarded client IP information.

Example backend log:

```text
BACKEND LOG: Client IP=127.0.0.1, Host=localhost, Forwarded For=127.0.0.1
```

### Nginx Configuration

The Nginx server block is stored in:

```text
nginx/reverseproxy.conf
```

Nginx forwards requests to the Flask backend using:

```nginx
proxy_pass http://127.0.0.1:5000;
```

The following headers are forwarded:

```nginx
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
```

### Verification

The reverse proxy was tested using:

```bash
curl http://localhost
```

The backend returned:

```text
Host = localhost
Real IP = 127.0.0.1
Forwarded For = 127.0.0.1
```

The backend's own terminal also displayed:

```text
BACKEND LOG: Client IP=127.0.0.1, Host=localhost, Forwarded For=127.0.0.1
```

This proves that the request reached the Flask backend through Nginx and that the configured proxy headers were received by the backend.

### Why the Client Does Not Talk Directly to the Backend

The client never talks to the backend directly because the backend application listens only on the local loopback address, `127.0.0.1:5000`, while Nginx is the publicly reachable entry point on port 80. When a client sends a request, Nginx receives it and forwards it to the backend while adding the `Host`, `X-Real-IP`, and `X-Forwarded-For` headers. This keeps the backend hidden from direct network access and allows Nginx to control and manage incoming requests. If `proxy_set_header X-Real-IP $remote_addr` were removed, the backend would no longer receive the client's IP address through the `X-Real-IP` header, so any application logic or logging that depends on that header would lose the original client IP.

## Project Structure

```text
nginx-infrastructure/
├── .gitignore
├── README.md
├── app.py
├── requirements.txt
└── nginx/
    └── reverseproxy.conf
```

## Technologies

* Ubuntu Linux
* Nginx
* Python
* Flask
* Git
* GitHub

