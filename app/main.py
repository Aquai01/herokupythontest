from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/test')
def index():
    return server.send_static_file('index.html')
