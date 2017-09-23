
# Invite & Register
## Setup Virtualenv
[Follow oficial intructions](https://virtualenv.pypa.io/en/stable/installation/)  
Then, create a virtualenv inside that folder and activate it
```bash
virtualenv .env -p python3
source .env/bin/activate
```
Install all dependecies
```bash
pip install -r requirements.txt
```

Privkey "identity" is registred and can generate invite tokens from it.

## Invite
Input: Passphrase
* Generate new Privkey
* Generate InvitationContent encrypting Passphrase with Privkey using [RSAES-PKCS1-v1_5](https://www.dlitz.net/software/pycrypto/api/current/Crypto.Cipher.PKCS1_v1_5-module.html)
* Generate InvitationKey exporting Privkey PEM [Ref](https://www.dlitz.net/software/pycrypto/api/current/Crypto.PublicKey.RSA._RSAobj-class.html#exportKey)
* Generate json Message with InvitationContent and InvitationKey
* Generate json envelope with Address
* Generate MessageSign of query and variables with my PubKey
* Put MessageSign as param
* Send GraphQL query
```bash
python invite.py
```
```
Privkey name (identity): #Leave blank
Passphrase (random): #Press enter
```
The script print mutation maded and token result
```
Invitation token: SVEV6gHt
```
## Register
Input: Token
* Generate json Message with Token
* Generate json envelope with my Address and my Pubkey
* Generate MessageSign of query and variables with my PubKey
* Put MessageSign as param
* Send GraphQL query
```bash
python register.py
```
```
Token: SVEV6gHt
Privkey Filename: 1 #Key name 
```
mutation's params and result are printed during execution
```
Registred success
```
You can find generated identity on ".identities" folder

## Invite & Registration Chaining
```bash
$ python invite.py
Privkey name (identity): 1
Passphrase (random): test
...
Invitation token: A4csVKEvPum

$ python register.py
Token: A4csVKEvPum
Privkey Filename: 2
...
Registred success

$ python invite.py
Privkey name (identity): 2
Passphrase (random): test2
...
Invitation token: hjoX3qogqypx
```