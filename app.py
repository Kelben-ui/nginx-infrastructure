from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():

    host = request.headers.get("Host")
    real_ip = request.headers.get("X-Real-IP")
    forwarded = request.headers.get("X-Forwarded-For")

    print(f"BACKEND LOG: Client IP={real_ip}, Host={host}, Forwarded For={forwarded}")

    return f"""
Host = {host}<br>
Real IP = {real_ip}<br>
Forwarded For = {forwarded}
"""

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
