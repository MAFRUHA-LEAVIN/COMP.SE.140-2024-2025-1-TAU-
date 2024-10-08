import os
import socket
import json
import requests
from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

def get_ip_address():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def get_running_processes():
    return subprocess.getoutput('ps -ax')

def get_disk_space():
    return subprocess.getoutput('df -h /')

def get_uptime():
    return subprocess.getoutput('uptime -p')

@app.route('/')
def service1_info():
    service1_data = {
        'Service1': {
            'ip_address': get_ip_address(),
            'running_processes': get_running_processes(),
            'disk_space': get_disk_space(),
            'uptime': get_uptime()
        }
    }

    # Fetch data from Service2
    try:
        service2_response = requests.get('http://service2:5000')
        service1_data['Service2'] = service2_response.json()
    except Exception as e:
        service1_data['Service2'] = str(e)

    return jsonify(service1_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8199)
