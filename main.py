from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/test')
def index():
    return "yo it works"

if __name__ == "__main__":
        app.run()