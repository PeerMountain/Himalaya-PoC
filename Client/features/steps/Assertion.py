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

def ghernik_vars(func):
    "Decorator to change interpretation of certain strings."
    def wrapper(context, *args):
        args = [
            context(arg[1:-1]) 
            if (
                arg.startswith('[') and arg.endswith(']')
            ) 
            else arg for arg in args
        ]
        return func(context, *args)
    return wrapper
                

@given("user attaches base64 encoded {string}")
def step(context, _object):
    context.object = _object


@when("we calculate SHA256 hash of {} as {}")
@ghernik_vars
def step(context, hashable, save_as):
    context[save_as] = b64encode(
        SHA256.new(hashable).digest()
    )

@then("we check {} and {} are equal")
@ghernik_vars
def step(context, a, b):
    assert a == b

@when('we encrypt {} using AES with key {} as {}')
@ghernik_vars
def step(context, to_encrypt, key, save_as):
    aes = AES(key)
    context[save_as] = aes.encrypt(to_encrypt)

@given('we print {}')
@ghernik_vars
def step(context, string):
    context['asd'] = 'a string'
    print(string)
