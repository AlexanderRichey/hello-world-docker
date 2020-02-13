from flask import Flask

app = Flask(__name__)

COUNT = 0

@app.route("/")
def hello():
    global COUNT
    COUNT += 1

    app.logger.debug("Count: %s", COUNT)

    return "Hello world!"
