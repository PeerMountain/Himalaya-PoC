import logging
from behave import (
    given,
    when,
    then,
)
from Crypto.Hash import SHA256
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
    setattr(context, save_as, aes.encrypt(to_encrypt))


@given('following private key as {} """{}"""')
@ghernik_vars
def step(context, save_as, sk_string):
    setattr(context, save_as, sk_string)


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
        RSA(sk_string).sign(to_sign)
    )


@when()
@ghernik_vars
def step(context):
    pass
