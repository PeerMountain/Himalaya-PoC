import logging
import json
import random
import datetime
from collections import OrderedDict

import msgpack
from behave import (
    given,
    when,
    then,
)
from Crypto.Hash import (
    SHA256,
    HMAC,
)
from TelefericClient.Cryptography import (
    RSA,
    AES,
)
from TelefericClient.Schema.Base.MessageContent import MessageContent
from TelefericClient.Schema.Base.MessageBody import MessageBody
from TelefericClient.Schema.Base.MessageEnvelope import MessageEnvelope
from TelefericClient.Schema.Base.Message import Message
from base64 import (
    b64encode,
    b64decode,
)

from TelefericClient.Client import Client
from TelefericClient.Identity import Identity


def ghernik_vars(func):
    "Decorator to change interpretation of certain strings."
    def wrapper(context, *args, **kwargs):
        args = [
            getattr(context, arg[1:-1]) if (
                arg.startswith('[') and arg.endswith(']')
            ) 
            else arg for arg in args
        ]
        return func(context, *args, **kwargs)
    return wrapper
                

@given("user attaches base64 encoded {}")
def step(context, _object):
    context.object = _object

@then("we calculate SHA256 hash of pack {} as {}")
@ghernik_vars
def step(context, hashable, save_as):
    if not isinstance(hashable, bytes):
        hashable = hashable.encode()
    setattr(context, save_as, b64encode(
        SHA256.new(hashable).digest()
    ))

@when("we calculate SHA256 hash of {} as {}")
@ghernik_vars
def step(context, hashable, save_as):
    if not isinstance(hashable, bytes):
        hashable = hashable.encode()
    setattr(context, save_as, b64encode(
        SHA256.new(hashable).digest()
    ))



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
    print(a,b)
    assert c == d

@when('we encrypt {} using AES with key {} as {}')
@ghernik_vars
def step(context, to_encrypt, key, save_as):
    aes = AES(key)
    setattr(
        context,
        save_as,
        aes.encrypt(to_encrypt.encode())
    )

@when('we encrypt {} usign RSA with key {} as {}')
@ghernik_vars
def step(context, to_encrypt, key, save_as):
    setattr(
        context,
        save_as,
        Identity(key).encrypt(to_encrypt.encode())
    )

@then('we encrypt {} using AES with key {} as {}')
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


@given('following private key as {}')
@ghernik_vars
def step(context, save_as):
    setattr(context, save_as, context.text.strip())

@given('following public key as {}')
@ghernik_vars
def step(context, save_as):
    setattr(context, save_as, context.text.strip())


@given('teleferic bootstrap node URI {}')
def step(context, uri):
    context.client = Client(uri, debug=True)


@given('teleferic signed timestamp as {}')
@ghernik_vars
def step(context, save_as):
    setattr(context, save_as, context.client.get_node_signedtimestamp())


@given('compose {} as')
@ghernik_vars
def step(context, save_as):
    setattr(
        context,
        save_as,
        context.text.strip().format(**context.__dict__)
    )


@given('compose {} as literal')
@ghernik_vars
def step(context, save_as):
    setattr(
        context,
        save_as,
        json.loads(context.text.strip())
    )


@when("I format {} with Message Pack as {}")
@ghernik_vars
def step(context, to_format, save_as):
    setattr(
        context,
        save_as,
        msgpack.packb(to_format)
    )


@when("I base64 encode {} as {}")
@ghernik_vars
def step(context, to_encode, save_as):
    setattr(
        context,
        save_as,
        b64encode(to_encode)
    )


@when("generate RSA signature {} using private_key {} of formated signable object {}")
@ghernik_vars
def step(context, save_as, sk_string, to_sign):
    setattr(
        context,
        save_as,
        RSA(sk_string).sign(to_sign).decode()
    )


@given("we set our identity with private key {}")
@ghernik_vars
def step(context, private_key):
    context.identity = Identity(private_key)

@then("we set our identity with private key {}")
@ghernik_vars
def step(context, private_key):
    context.identity = Identity(private_key)


@given('we create identity {} with private key {}')
@ghernik_vars
def step(context, save_as, private_key):
    setattr(
        context,
        save_as,
        Identity(private_key)
    )


@given("we generate a random {} byte salt for each element in {} as {}")
@ghernik_vars
def step(context, salt_length, object_list, save_as):
    setattr(
        context,
        save_as,
        [
            "".join([
                chr(random.randint(0, 255))
                for _ in range(int(salt_length))
            ]) for _ in range(len(object_list))
        ]
    )

@given('we pack every element in {} with Message Pack as {}')
@ghernik_vars
def step(context, object_list, save_as):
    setattr(
        context,
        save_as,
        [
            msgpack.packb(item) for item in object_list
        ]
    )

@given("we calculate salted hash for each element in {} with salts {} as {}")
@ghernik_vars
def step(context, object_list, salt_list, save_as):
    setattr(
        context,
        save_as,
        [
            b64encode(
                HMAC.new(
                    salt_list[i].encode(),
                    object_list[i],
                    SHA256
                ).digest()
            )
            for i in range(len(object_list))
        ]
    )

@then('we include salts {} in meta list {} as {}')
@ghernik_vars
def step(context, salt_list, meta_list, save_as):
    for i, salt in enumerate(salt_list):
        meta_list[i] = b64encode(
            msgpack.packb(
                msgpack.unpackb(meta_list[i]).update({
                    'metaSalt': salt
                })
            )
        )
    setattr(
        context,
        save_as,
        meta_list
    )

@given("{} is integer {}")
@ghernik_vars
def step(context, save_as, origin):
    setattr(
        context,
        save_as,
        int(origin)
    )

@given("{} is string {}")
@ghernik_vars
def step(context, save_as, origin):
    setattr(
        context,
        save_as,
        str(origin)
    )

@given("{} is the address of {}")
@ghernik_vars
def step(context, save_as, key):
    setattr(
        context,
        save_as,
        Identity(key).address
    )

@given("{} is object {}")
@ghernik_vars
def step(context, save_as, origin):
    setattr(
        context,
        save_as,
        origin
    )

@given('timestamped signature of {} as {}')
@ghernik_vars
def step(context, to_sign, save_as):
    print(context.identity.address,to_sign,save_as)
    setattr(
        context,
        save_as,
        context.identity.sign_message(
            to_sign, context.client
        )
    )

@when('we pack {} with message pack as {}')
@ghernik_vars
def step(context, data_dict, save_as):
    setattr(
        context,
        save_as,
        msgpack.packb(data_dict)
    )

@given('random 40 bytes salt for example {} as {}')
@ghernik_vars
def step(context, salt, save_as):
    setattr(
        context,
        save_as,
        bytes(bytearray.fromhex(salt.replace(':', '')))
    )

@given('random {} bytes salt as {}')
@ghernik_vars
def step(context, salt_length, save_as):
    setattr(
        context,
        save_as,
        "".join([
            chr(random.randint(0, 255))
            for _ in range(int(salt_length))
        ]).encode()
    )

@given('{} is random string form example {}')
@ghernik_vars
def step(context, save_as, rnd_string):
    setattr(
        context,
        save_as,
        str(rnd_string)
    )

@given('following graphql query as {}')
@ghernik_vars
def step(context, save_as):
    setattr(
        context,
        save_as,
        context.text.strip()
    )

@when('we compose {} with following keys')
@ghernik_vars
def step(context, save_as):
    obj = OrderedDict()
    for row in context.text.strip().split('\n'):
        k, v = row.split(':')
        value = getattr(context, v.strip()[1:-2])
        obj[k.strip().strip('"').strip("'")] = value
    setattr(
        context,
        save_as,
        obj
    )

@when('we send {} with variables {} to bootstrap node')
@ghernik_vars
def step(context, query, variables):
    context.response = context.client.request(query,variables)
    
@then('server should response success')
@ghernik_vars
def step(context):
    assert context.response.get('error') == None


@given('one or more {}')
@ghernik_vars
def step(context, x):
    pass

@given('{} for each one')
@ghernik_vars
def step(context,var):
    pass

@then('we compose a list of {} as {}')
@ghernik_vars
def step(context,item,save_as):
    setattr(
        context,
        save_as,
        [item]
    )


@then('we compose {} with following keys')
@ghernik_vars
def step(context, save_as):
    obj = OrderedDict()
    for row in context.text.strip().split('\n'):
        k, v = row.split(':')
        value = getattr(context, v.strip()[1:-2])
        obj[k.strip().strip('"').strip("'")] = value
    setattr(
        context,
        save_as,
        obj
    )

@when('we calculate HMAC-SHA256 of {} with {} as {}')
@ghernik_vars
def step(context, pack, salt, save_as):
    setattr(
        context,
        save_as,
        b64encode(
            HMAC.new(
                salt,
                pack,
                SHA256
            ).digest()
        )
    )

@then('we calculate HMAC-SHA256 of {} with {} as {}')
@ghernik_vars
def step(context, pack, salt, save_as):
    setattr(
        context,
        save_as,
        b64encode(
            HMAC.new(
                salt,
                pack,
                SHA256
            ).digest()
        )
    )

@given("{} is datetime {}")
@ghernik_vars
def step(context, save_as, date_string):
    setattr(
        context,
        save_as,
        datetime.datetime.strptime(date_string, "%Y-%m-%d")
    )

@when("we format {} with iso formated string as {}")
@ghernik_vars
def step(context, origin_date, save_as):
    setattr(
        context,
        save_as,
        origin_date.isoformat()
    )

@when('we XAdES-T sign {} as {}')
@ghernik_vars
def step(context, to_sign, save_as):
    signature = context.identity.sign_message(
        to_sign, context.client
    )
    setattr(
        context,
        save_as,
        signature
    )

@then('we compose {} with keys')
@ghernik_vars
def step(context, save_as):
    obj = OrderedDict()
    for row in context.text.strip().split('\n'):
        k, v = row.split(':')
        value = getattr(context, v.strip()[1:-2])
        if isinstance(value, bytes):
            value = value.decode()
        elif isinstance(value, list):
            value = [
                val if not isinstance(val, bytes) else val.decode()
                for val in value
            ]
        obj[k.strip().strip('"').strip("'")] = value
    setattr(
        context,
        save_as,
        obj
    )

@given('context var {} is {}')
@ghernik_vars
def step(context, save_as, value):
    setattr(
        context,
        save_as,
        value
    )


@when('we compose assertion message body {} with assertions {} and body type {}')
@ghernik_vars
def step(context, save_as, assertions, body_type):
    setattr(
        context,
        save_as,
        MessageBody(
            body_type=int(body_type),
            assertions=assertions
        )
    )

@when('we compose message content {} with {} and message type {}')
@ghernik_vars
def step(context, save_as, message_body, message_type):
    setattr(
        context,
        save_as,
        MessageContent(
            message_type=message_type,
            message_body=message_body
        )
    )


@when('we set {} as list')
@ghernik_vars
def step(context, save_as):
    setattr(
        context,
        save_as,
        list()
    )


@when('we append {} to {}')
@ghernik_vars
def step(context, to_append, _list):
    _list.append(to_append)


@when('we compose message with {}, passphrase {}, readers {} and containers {}')
@ghernik_vars
def step(context, message_content, passphrase, readers, containers):
    context.message = Message(
        message_content,
        passphrase,
        readers,
        containers
    )


@then('we send {} to teleferic with container key {} and save response as {}')
@ghernik_vars
def step(context, message, container_key, save_response_as):
    envelope = MessageEnvelope(context.identity, context.client.node, container_key)
    envelope.message = message
    response = envelope.send()
    setattr(
        context,
        save_response_as,
        response
    )


@then('response {} is OK')
@ghernik_vars
def step(context, response):
    assert response

@given('we pass')
def step(context):
    pass