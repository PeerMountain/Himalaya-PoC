# Sources
* https://unix.stackexchange.com/questions/119967/rsa-2048-keypair-generation-via-openssl-0-5s-via-gpg-30s-why-the-difference

# Commands
## Create a key
```bash
openssl genrsa -out c_1024.private 1024
openssl rsa -in c_1024.private -pubout -out c_1024.public
```