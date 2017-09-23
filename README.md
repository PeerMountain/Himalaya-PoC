# Himalaya
## Add user to registry
```bash
root@peer-mountain01 ~ # docker run --entrypoint htpasswd registry:2 -Bbn user pass >> /opt/registry/auth/htpasswd
```