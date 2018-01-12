import logging
from behave import (
    given,
    when,
    then,
)
from Crypto.Hash import (
    SHA256,
    HMAC,
)
from base64 import (
    b64encode,
    b64decode,
)

from Client import Client


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
                

@given("user attaches base64 encoded {string}")
def step(context, _object):
    context.object = _object


@when("we calculate SHA256 hash of {} as {}")
@ghernik_vars
def step(context, hashable, save_as):
    setattr(context, save_as, b64encode(
        SHA256.new(hashable).digest()
    ))


@then("we check {} and {} are equal")
@ghernik_vars
def step(context, a, b):
    assert a == b

@when('we encrypt {} using AES with key {} as {}')
@ghernik_vars
def step(context, to_encrypt, key, save_as):
    aes = AES(key)
    setattr(context, save_as, aes.encrypt(to_encrypt)


@given('following private key as {}')
@ghernik_vars
def step(context, save_as):
    setattr(context, save_as, context.text.strip())


@given('teleferic bootstrap node URI {}')
def step(context, uri):
    context.client = Client(uri)


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


@when("I format {} with Message Pack as {}")
@ghernik_vars
def step(context, to_format, save_as)
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


@when("we set our identity with private key {}")
@ghernik_vars
def step(context, private_key):
    context.identity = Identity(private_key)


@when("we calculate {} byte salt for each meta in {} as {}")
@ghernik_vars
def step(context, salt_length, object_list, save_as):
    setattr(
        context,
        save_as,
        [
            "".join(chr(random.randint(0, 255) for _ in range(int(length))))
            for _ in range(len(meta_list))
        ]
    )

@when("we calculate salted hash for each element in {} with salts {} as {}")
@ghernik_vars
def step(context, object_list, salt_list, save_as):
    setattr(
        context,
        save_as,
        [
            HMAC.new(
                salt_list[i],
                object_list[i],
                SHA256
            ).digest().decode()
            for i in range(len(object_list))
        ]
    )

@when('we include salts {} in meta list {} as {}')
@ghernik_vars
def step(context, salt_list, meta_list, save_as):
    for i, salt in enumerate(salt_list):
        meta_list[i].update({
            'metaSalt': salt
        })
    setattr(
        context,
        save_as,
        meta_list
    )

@given("{} is datetime {}")
@ghernik_vars
def step(context, save_as, date_string):
    setattr(
        context,
        save_as,
        datetime.strptime(date_string).replace(tzinfo=datetime.timezone.utc)
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

@given('we pass')
def step(context):
    pass