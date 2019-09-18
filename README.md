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
```
