import os
import time
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():

    host = request.headers.get("Host")
    real_ip = request.headers.get("X-Real-IP")
    forwarded = request.headers.get("X-Forwarded-For")
    port = request.environ.get("SERVER_PORT")

    print(f"BACKEND LOG: Client IP={real_ip}, Host={host}, Forwarded For={forwarded}")

    return f"""
Backend Port = {port}<br>
Host = {host}<br>
Real IP = {real_ip}<br>
Forwarded For = {forwarded}
"""

@app.route("/slow")
def slow():

    time.sleep(10)

    port = request.environ.get("SERVER_PORT")

    return f"Backend Port = {port}<br>Slow request completed"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="127.0.0.1", port=port)
