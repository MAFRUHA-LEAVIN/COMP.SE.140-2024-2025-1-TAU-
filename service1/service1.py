from flask import Flask, jsonify, request
import socket
import os
import psutil
import time
from threading import Thread
from werkzeug.serving import make_server

app = Flask(__name__)

@app.route("/service1")
def service1_status():
    # Get IP address
    ip_address = socket.gethostbyname(socket.gethostname())
    
    # List running processes (limit to 5 for brevity)
    processes = [proc.info for proc in psutil.process_iter(['pid', 'name'])][:5]
    
    # Disk space information
    disk_usage = psutil.disk_usage('/')
    disk_space = {
        "total": disk_usage.total,
        "used": disk_usage.used,
        "free": disk_usage.free,
        "percent": disk_usage.percent
    }
    
    # Uptime calculation
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_formatted = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))
    
    # JSON response with system info
    service1_data = {
        "ip_address": ip_address,
        "processes": processes,
        "disk_space": disk_space,
        "uptime_seconds": uptime_seconds,
        "uptime": uptime_formatted
    }

    return jsonify(service1_data)

@app.route("/shutdown", methods=["POST"])
def shutdown():
    shutdown_server()
    return "Service shutting down...", 200

def shutdown_server():
    func = request.environ.get("werkzeug.server.shutdown")
    if func is None:
        raise RuntimeError("Not running with the Werkzeug Server")
    func()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Listen on all interfaces and port 5000
