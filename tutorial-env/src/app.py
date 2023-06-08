from flask import Flask,jsonify, render_template
import socket
app = Flask(__name__)

def fetchdetails():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return str(hostname), str(host_ip)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/statusinfo")
def statusinfo():
    return jsonify(
        status = "up"
    )

@app.route("/detailedinfo")
def detailedinfo():
    hostname, ip = fetchdetails()
    return render_template('index.html', HOSTNAME = hostname, IP=ip)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    