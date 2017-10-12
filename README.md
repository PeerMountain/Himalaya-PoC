# Himalaya
## Add user to registry
```bash
root@peer-mountain01 ~ # docker run --entrypoint htpasswd registry:2 -Bbn user pass >> /opt/registry/auth/htpasswd
```
## Generate graphql docs
```bash
$ graphdoc -e http://teleferic.local:8000/teleferic -o ../Docs --force
```
## Build images
```bash
$ docker-compose build
```
## Push images to registry
### Ngxin gateway
```bash
$ docker tag himalaya_gateway meteoro.dxmarkets.com:5000/himalaya_gateway
$ docker push meteoro.dxmarkets.com:5000/himalaya_gateway:latest
```
### Teleferic
```bash
$ docker tag himalaya_teleferic meteoro.dxmarkets.com:5000/himalaya_teleferic
$ docker push meteoro.dxmarkets.com:5000/himalaya_teleferic:latest
```
## Pull images from registry
### Nginx gateway
```bash
$ docker pull meteoro.dxmarkets.com:5000/himalaya_gateway:latest
```
### Teleferic
```bash
$ docker pull meteoro.dxmarkets.com:5000/himalaya_teleferic:latest
```
## Update running containers
```bash
$ docker-compose up --build -d
```
## Load Teleferic Persona
```bash
$ docker exec himalaya_teleferic_1 python manage.py loaddata genesis_identity.json
```