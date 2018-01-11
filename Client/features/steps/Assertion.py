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


@given("user attaches base64 encoded {string}")
def step(context, _object):
    context.object = _object


@when("we calculate SHA256 hash of {} as <{(\w+)}>")
def step(context, hashable, save_as):
    context[save_as] = b64encode(
        SHA256.new(hashable).digest()
    )

@then("we check {} and {} are equal")
def step(context, a, b):
    assert a == b