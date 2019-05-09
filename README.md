# Docker Flask app

Dockerized Flask app deployed to AWS ECS as production.

### Startup

Starting dependencies
```
docker-compose up -d
```

Building and starting service
```
docker build -t server:v0 .
docker run -d -p 5000:5000 --name docker-flask server:v0
```
Hit http://localhost:5000/health

Debugging
```
# volume mount local changes to docker container
docker run -d -v ${pwd}:/app -p 5000:5000 --name docker-flask abe45552866e
# ALT: enter running docker container to modify files
docker exec -it docker-flask /bin/sh
```

### Tech Stack

* Docker - containerization
* Flask - server
* React - client
* Mongo - database
* Protobuf - serialization (alt: [Marshmallow](https://marshmallow.readthedocs.io/en/3.0/))
