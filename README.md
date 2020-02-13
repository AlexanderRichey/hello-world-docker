# hello-world-docker

A containerized hello-world application based on Flask. Flask runs behind a production-ready Gunicorn server.

```
# Clone the repo
$ git clone git@github.com:AlexanderRichey/hello-world-docker.git
$ cd hello-world-docker

# Build and tag the docker image
$ docker build -t hello .

# Run the image
$ docker run -p 5000:5000 hello

# Run in development mode
$ docker run -p 5000:5000 -v $(pwd):/var/www -e FLASK_APP=hello.py -e FLASK_ENV=development hello flask run --host 0.0.0.0
```
