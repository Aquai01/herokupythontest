from flask import Flask, request, abort

server = Flask(__name__)

@server.route('/test')
def index():
    return server.send_static_file('index.html')

