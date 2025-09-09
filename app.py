from flask import Flask
import time
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from Flask on Kubernetes!"

@app.route('/load')
def load():
    def burn_cpu():
        end = time.time() + 10
        while time.time() < end:
            pass
    thread = threading.Thread(target=burn_cpu)
    thread.start()
    return "CPU load triggered!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
