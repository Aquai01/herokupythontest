from flask import Flask, request, abort

server = Flask(__name__)

@server.route('/test')
def index():
    return server.send_static_file('index.html')

if __name__ == '__main__':
    server.run(debug=False, host="0.0.0.0", port="5000")
