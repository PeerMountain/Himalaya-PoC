import logging
import json
import random
import datetime
from collections import OrderedDict
from contextlib import suppress

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
from TelefericClient.Schema.Assertion import Assertion
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

@then("we check {} and {} salts should be equal")
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
    print(c,len(c))
    print(d,len(d))
    #bytes(bytearray.fromhex(salt.replace(':', '')))
    assert c == d

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

@when('we encrypt {} usign RSA with key {} as {}')
@ghernik_vars
def step(context, to_encrypt, key, save_as):
    setattr(
        context,
        save_as,
        Identity(key).encrypt(
            to_encrypt.encode()
            if isinstance(to_encrypt, str)
            else to_encrypt
        )
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
    context.client = Client(uri, debug=False)


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


@when('we decode {} with base64 as {}')
@ghernik_vars
def step(context, to_decode, save_as):
    setattr(
        context,
        save_as,
        b64decode(to_decode)
    )

@then('we decode {} with base64 as {}')
@ghernik_vars
def step(context, to_decode, save_as):
    setattr(
        context,
        save_as,
        b64decode(to_decode)
    )

@when("I base64 encode {} as {}")
@ghernik_vars
def step(context, to_encode, save_as):
    setattr(
        context,
        save_as,
        b64encode(to_encode)
    )


@when("we base64 decode {} as {}")
@ghernik_vars
def step(context, to_encode, save_as):
    setattr(
        context,
        save_as,
        b64decode(to_encode)
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
    setattr(
        context,
        save_as,
        context.identity.sign_message(
            to_sign, context.client
        )
    )

@then(u'we create a timestamped signature of {} as {}')
@ghernik_vars
def step(context, to_sign, save_as):
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

@when('we unpack {} with message pack as {}')
@ghernik_vars
def step(context, byte_array, save_as):
    setattr(
        context,
        save_as,
        msgpack.unpackb(byte_array)
    )

@then('we unpack {} with message pack as {}')
@ghernik_vars
def step(context, byte_array, save_as):
    setattr(
        context,
        save_as,
        msgpack.unpackb(byte_array)
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

@given('{} and {} acl rules')
@ghernik_vars
def step(context, acl_rule_1, acl_rule_2):
    pass

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
    
@then('server should response {}')
def step(context,status):
    print(context.response.get('errors'))
    if status == 'success':
        assert context.response.get('errors') == None
    elif status == 'failure':
        assert context.response.get('errors') != None
    else:
        raise Exception('Response can be success or failure not %s' % status)

@given('sent message hash as {}')
@ghernik_vars
def step(context, save_as):
    setattr(
        context,
        save_as,
        context.response.get('data').get('sendMessage').get('messageHash')
    )


@given('one or more {}')
@ghernik_vars
def step(context, x):
    pass

@given('{} for each one')
@ghernik_vars
def step(context,var):
    pass

@then('we compose a list of acl rules as {}')
@ghernik_vars
def step(context,save_as):
    setattr(
        context,
        save_as,
        [context.reader_acl_rule,context.sender_acl_rule]
    )

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
    if isinstance(salt, str):
        salt = salt.encode()
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

@given("assertion by {} to {} with hash as {}")
@ghernik_vars
def step(context, sender_sk, reader_pk, save_as):
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    meta = OrderedDict()
    meta['metaType'] = 2
    meta['metaValue'] = 'Pepe Sarasa'
    assertion = Assertion(
        Identity(sender_sk),
        context.client,
        [
            {
                'valid_until': now.isoformat(),
                'retain_until': tomorrow.isoformat(),
                'object': b'\x12\x34\x56\x78\x90',
                'metas': [meta]
            }
        ],
        [
            Identity(reader_pk),
        ]
    )
    response = assertion.send()
    try:
        setattr(
            context,
            save_as,
            response.get('data').get('sendMessage').get('messageHash')
        ) 
    except Exception as e:
        logging.warning("Request failed.")
        raise


@given('we retrieve message with hash {}')
@ghernik_vars
def step(context, _hash):
    query = """
    query{
        messageByHash(messageHash: "%s") {
            messageHash
            messageType
            messageSig
            dossierHash
            bodyHash
            message
            createdAt
            ACL{
                reader{
                    address
                }
                key
            }
            objects{
                containerHash
                objectHash
                containerSig
                objectContainer
                metaHashes
            }
        }
    }
    """ % _hash
    response = context.client.request(query)
    setattr(
        context,
        'envelope',
        response.get('data').get('messageByHash')
    )

@given('we get key from ACL for our address as {}')
@ghernik_vars
def step(context, save_as):
    key = next(
        filter(
            lambda x: x.get('reader').get('address') == context.identity.address,
            context.envelope.get('ACL')
        )
    )
    setattr(
        context,
        save_as,
        key.get('key')
    )


@given('we decrypt {} with our identity as {}')
@ghernik_vars
def step(context, encrypted_data, save_as):
    setattr(
        context,
        save_as,
        context.identity.decrypt(encrypted_data)
    )


@given('we get the encrypted message content as {}')
@ghernik_vars
def step(context, save_as):
    setattr(
        context,
        save_as,
        context.envelope.get('message')
    )

@given('we extract message body from {} as {}')
@ghernik_vars
def step(context, message_content, save_as):
    setattr(
        context,
        save_as,
        msgpack.unpackb(
            b64decode(
                message_content.get(b'messageBody')
            )
        )
    )


@given('we extract assertions from {} as {}')
@ghernik_vars
def step(context, message_body, save_as):
    setattr(
        context,
        save_as,
        message_body.get(b'assertions')
    )


@given('we extract containers from message envelope as {}')
@ghernik_vars
def step(context, save_as):
    setattr(
        context,
        save_as,
        context.envelope.get(b'containers')
    )


@given('we decrypt {} with AES module {} as {}')
@ghernik_vars
def step(context, encrypted_data, aes_key, save_as):
    cipher = AES(aes_key)
    try:
        setattr(
            context,
            save_as,
            cipher.decrypt(b64decode(encrypted_data))
        )
    except Exception:
        setattr(
            context,
            save_as,
            cipher.decrypt(encrypted_data)
        )

@given('we extract first value from {} as {}')
@ghernik_vars
def step(context, _list, save_as):
    setattr(
        context,
        save_as,
        _list[0]
    )

@given('we extract value {} from {} as {}')
@ghernik_vars
def step(context, key, _dict, save_as):
    setattr(
        context,
        save_as,
        _dict.get(key, _dict.get(key.encode()))
    )

@given('we remove value {} from {}')
@ghernik_vars
def step(context, key, _dict):
    with suppress(KeyError):
        del _dict[key]
    with suppress(KeyError):
        del _dict[key.encode()]


@then('we replace value {} of {} with {}')
@given('we replace value {} of {} with {}')
@ghernik_vars
def step(context, value_name, _dict, new_value):
    _dict[value_name] = new_value


@given('{} is address of {}')
@ghernik_vars
def step(context, save_as, identity):
    setattr(
        context,
        save_as,
        identity.address
    )


@when('we compact access control list {} as follows')
@ghernik_vars
def step(context, acl):
    context.access_control_list = [
        {
            'reader': el['reader']['address'] if isinstance(el['reader'], dict) else el['reader'],
            'key': el['key']
        } for el in context.access_control_list
    ]
@then('we break')
def step(context):
    import pdb; pdb.set_trace()

@then('we store resultant property {} as {}')
@ghernik_vars
def step(context, property_path, save_as):
    result = context.response
    path_parts = property_path.split('.')
    for part_key in path_parts:
        result = result.get(part_key)
    setattr(
        context,
        save_as,
        result
    )

@when('we get key from ACL for our address as {}')
@ghernik_vars
def step(context, save_as):
    key = next(
        filter(
            lambda x: x.get('reader').get('address') == context.identity.address,
            context.envelope.get('ACL')
        )
    )
    setattr(
        context,
        save_as,
        key.get('key')
    )

@when('we decrypt {} usign RSA as {}')
@ghernik_vars
def step(context, encrypted_data, save_as):
    setattr(
        context,
        save_as,
        context.identity.decrypt(encrypted_data)
    )

@given('property {} from {} as {}')
@ghernik_vars
def step(context,property_path, object, save_as):
    result = object
    path_parts = property_path.split('.')
    for part_key in path_parts:
        aux = result.get(part_key)
        if aux is None:
            aux = result.get(part_key.encode())
        if aux is None:
            raise Exception('Property %s is not defined on %s.' % (property_path,object))
        result = aux
    setattr(
        context,
        save_as,
        result
    )

@when('we decrypt {} with AES module {} as {}')
@ghernik_vars
def step(context, encrypted_data, aes_key, save_as):
    cipher = AES(aes_key)
    setattr(
        context,
        save_as,
        cipher.decrypt(encrypted_data)
    )

@then('the signature RSA {} is valid for the pack {} with the public key {} should be valid')
@ghernik_vars
def step(context, signature, pack, key):
    idn = Identity(key)
    assert idn.verify(pack,signature)


@when('we get integer index {} from vector {} as {}')
@ghernik_vars
def step(context, index, vector, save_as):
    setattr(
        context,
        save_as,
        vector[int(index)]
    )

@given('integer index {} from vector {} as {}')
@ghernik_vars
def step(context, index, vector, save_as):
    setattr(
        context,
        save_as,
        vector[int(index)]
    )

@when('we filter vector {} searching {} on property {} as {}')
@ghernik_vars
def step(context, vector, searching, property_path, save_as):
    if type(searching) != bytes:
        searching = searching.encode()
    result = False
    for item in vector:
        setattr(
            context,
            'aux_in',
            item
        )
        context.execute_steps('''
            Given property %s from [aux_in] as aux_out
        ''' % property_path)
        if type(context.aux_out) != bytes:
            setattr(
                context,
                'aux_out',
                context.aux_out.encode()
            )
        if context.aux_out == searching :
            result = item
            break
    if result == False:
        raise Exception('Value %s is not defined on %s preperty of %s.' % (searching,object,property_path))
    setattr(
        context,
        save_as,
        result
    )

@then('print {}')
@ghernik_vars
def step(context, to_print):
    print(to_print)
    assert False