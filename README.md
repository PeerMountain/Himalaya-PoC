# Himalaya
## Add Registry server
```bash
docker run -d \
  -p 5000:5000 \
  --restart=always \
  --name registry \
  -v /opt/registry/auth:/auth \
  -e "REGISTRY_AUTH=htpasswd" \
  -e "REGISTRY_AUTH_HTPASSWD_REALM=Registry Realm" \
  -e REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd \
  -v /etc/ssl/wildcard/:/certs \
  -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/server.crt \
  -e REGISTRY_HTTP_TLS_KEY=/certs/server.key \
  registry:2
```
## Add user to registry
```bash
root@peer-mountain01 ~ # docker run --entrypoint htpasswd registry:2 -Bbn user pass >> /opt/registry/auth/htpasswd
```
## Generate graphql docs
```bash
$ graphdoc -e http://teleferic.local:8000/teleferic -o ./Docs --force
```
## Build images
```bash
$ docker-compose build
```
## Push images to registry
### Ngxin gateway
```bash
$ docker push meteoro.dxmarkets.com:5000/himalaya_gateway:latest
```
### Teleferic
```bash
$ docker push meteoro.dxmarkets.com:5000/himalaya_teleferic:latest
```
## Update Swarm
```bash
$ docker stack deploy -c docker-compose.himalaya.yml himalaya_dev --with-registry-auth
```
### Nginx gateway
```bash
$ docker service update himalaya_dev_gateway --with-registry-auth --update-order start-first --detach=false
```
### Teleferic
```bash
$ docker service update himalaya_dev_teleferic --with-registry-auth --update-order start-first --detach=false
```

## Some commands
```bash
#list services
$ docker service ls
#Inspect
$ docker service inspect himalaya_dev_gateway  --pretty
$ docker service inspect himalaya_dev_teleferic  --pretty
#Scale
$ docker service scale himalaya_dev_gateway=2
$ docker service scale himalaya_dev_teleferic=3
```

#Monitorion
## Start and Deploy
```bash
$ docker stack deploy -c docker-compose.cloud_dashboard.yml monitor
```
## Access
Go to [Grafana](http://94.130.38.47:8443)
user: nacho
pass: X53unbuxSRrVxv31A8bX
## Stop and remove
```bash
$ docker stack rm monitor
```


add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"