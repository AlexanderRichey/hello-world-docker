import os
from flask import Flask

app = Flask(__name__)

COUNT = 0


@app.route("/")
def hello():
    global COUNT
    COUNT += 1
    danger = os.environ
    return f"""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>hello world</title>
    <!-- <link rel="stylesheet" href="https://newcss.net/new.min.css"> -->
  </head>
  <body>
    <h1>Hello world {COUNT} times!</h1>
    <p>Here is my environment:</p>
    <p><pre>{danger}</pre></p>
  </body>
</html>
    """
