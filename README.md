# Fastapi Production Line
A Rest API apllication that uses fastapi and pydantic in backend.

## Run Application
Clone the repo
```shell
git clone https://github.com/zereaykut/Fastapi-Production-Line
cd Fastapi-Production-Line
```

Create docker image
```shell
docker build -t production-line-docker-image .
```

Run docker image
```shell
docker run -d --name production-line-docker-container -p 80:80 production-line-docker-image
```

Application can be accessed from http://127.0.0.1:8000

## Application Docs
Application docs can be accessed on http://127.0.0.1:8000/docs

## If docker service not running
Start Docker Service and Enable.
```shell
sudo systemctl start docker.service
sudo systemctl enable docker.service
```

## Note 
If you see this message:
```shell
docker: permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/create": dial unix /var/run/docker.sock: connect: permission denied.
See 'docker run --help'.
```
That's because you need to either run the docker command with sudo or add the user to docker group to run docker commands without sudo.
