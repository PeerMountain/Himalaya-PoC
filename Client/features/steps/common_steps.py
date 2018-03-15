import os

from libs import ghernik_vars

from TelefericClient.Cryptography import (
    RSA,
    AES,
)
from TelefericClient.Client import Client
from TelefericClient.Identity import Identity


@then(u'we set {} identity with RSA key {}')
@ghernik_vars
def step(context, save_as, key):
    print(key)
    setattr(
        context,
        save_as,
        Identity(key)
    )


@given(u'{} is URI {}')
@ghernik_vars
def step(context, save_as, origin):
    setattr(
        context,
        save_as,
        str(origin)
    )


@when(u'we send {} with variables {} to bootstrap node {} and store the response as {}')
@ghernik_vars
def step(context, query, variables, uri, save_as):
    client = Client(uri, debug=False)
    response = client.request(query, variables)
    setattr(
        context,
        save_as,
        response
    )


@when(u'we send {} to bootstrap node {} and store the response as {}')
@ghernik_vars
def step_impl(context, query, uri, save_as):
    client = Client(uri, debug=False)
    response = client.request(query)
    setattr(
        context,
        save_as,
        response
    )

@then(u'{} response should be {}')
@ghernik_vars
def step_impl(context, response, expected):
    if expected == 'success':
        assert response.get('errors') == None
    elif expected == 'failure':
        assert response.get('errors') != None
    else:
        raise Exception('Response can be success or failure not %s' % expected)

@given(u'{} is address {}')
@ghernik_vars
def step(context, save_as, origin):
    setattr(
        context,
        save_as,
        str(origin)
    )

@given(u'{} is url {}')
@ghernik_vars
def step(context, save_as, origin):
    setattr(
        context,
        save_as,
        str(origin)
    )


@when(u'we sign {} using PKCS1 v1.5 with key {} as {}')
@ghernik_vars
def step(context, content, key, save_as):
    idn = Identity(key)    
    setattr(
        context,
        save_as,
        idn.sign(content)
    )

@when(u'we encrypt {} using RSA with key {} as {}')
@ghernik_vars
def step(context, content, key, save_as):
    idn = Identity(key)    
    setattr(
        context,
        save_as,
        idn.encrypt(content)
    )

@when('we calculate public key of {} as {}')
@ghernik_vars
def step(context, key, save_as):
    idn = Identity(key)    
    setattr(
        context,
        save_as,
        idn.pubkey
    )

@given('{} as the address of {}')
@ghernik_vars
def step(context, save_as, key):
    setattr(
        context,
        save_as,
        Identity(key).address
    )

@given('{} as the public key of {}')
@ghernik_vars
def step(context, save_as, key):
    setattr(
        context,
        save_as,
        Identity(key).pubkey
    )

@given('random {} bytes salt as {}')
@ghernik_vars
def step(context, str_salt_length, save_as):
    salt_length = int(str_salt_length)
    setattr(
        context,
        save_as,
        bytes(bytearray(os.urandom(salt_length)))
    )


@then("we check {} and {} should be equal")
@ghernik_vars
def step(context, a, b):
    if type(a) is bytes:
        c = a.decode()
    else:
        c = a
    if type(b) is bytes:
        d = b.decode()
    else:
        d = b
    assert c == d

@when('we encrypt {} using AES with key {} as {}')
@ghernik_vars
def step(context, to_encrypt, key, save_as):
    aes = AES(key)
    if not isinstance(to_encrypt, bytes):
        to_encrypt = to_encrypt.encode()
    setattr(
        context,
        save_as,
        aes.encrypt(to_encrypt)
    )

@given('new private key as {}')
@ghernik_vars
def step(context, save_as):
    setattr(
        context,
        save_as,
        Identity().privkey
    )

@given("{} is string {}")
@ghernik_vars
def step(context, save_as, origin):
    setattr(
        context,
        save_as,
        str(origin).encode()
    )
