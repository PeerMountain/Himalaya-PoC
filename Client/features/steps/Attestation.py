from collections import OrderedDict
import datetime

from behave import given, then

from Assertion import ghernik_vars
from TelefericClient.Identity import Identity
from TelefericClient.Client import Client
from TelefericClient.Schema.Assertion import Assertion


@given('Sender Identity with following private key as {}')
@ghernik_vars
def step(context, save_as):
    sender = Identity(context.text.strip())
    setattr(context, save_as, sender)


@given('Reader Identity with following private key as {}')
@ghernik_vars
def step(context, save_as):
    reader = Identity(context.text.strip())
    setattr(context, save_as, reader)


@given('following metaType as {}')
@ghernik_vars
def step(context, save_as):
    setattr(context, save_as, context.text.strip())


@given('following metaValue as {}')
@ghernik_vars
def step(context, save_as):
    setattr(context, save_as, context.text.strip())


@given('following object as {}')
@ghernik_vars
def step(context, save_as):
    setattr(context, save_as, context.text.strip())


@then('we compose and send an Assertion storing the messageHash as {}')
@ghernik_vars
def step(context, save_as):
    now = datetime.datetime.now(datetime.timezone.utc)
    tomorrow = now + datetime.timedelta(days=1)

    readers = [context.idn_reader]

    assertion_object = [{
        'valid_until': now.isoformat(),
        'retain_until': tomorrow.isoformat(),
        'object': bytes(context.object.encode()),
        'metas': [{
            'metaType': context.meta_type,
            'metaValue': context.meta_value,
        }]
    }]

    assertion = Assertion(
        context.idn_sender,
        context.client,
        assertion_object,
        readers
    )
    response = assertion.send()
    message_hash = response['data']['sendMessage']['messageHash']

    setattr(context, save_as, message_hash)


@then('we retrive the previous Assertion data as {}')
@ghernik_vars
def step(context, save_as):
    query = """
    query{
        messageByHash(messageHash: "%s") {
            messageHash
            messageType
            messageSign
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
                objectHash
                metaHashes
                container {
                    containerHash
                    containerSign
                    objectContainer
                }
            }
        }
    }
    """ % context.assertion_message_hash

    response = context.client.request(query)
    setattr(context, save_as, response['data']['messageByHash'])


@given('Assertion objectHash as {}')
@ghernik_vars
def step(context, save_as):
    setattr(
        context,
        save_as,
        context.assertion_data['objects'][0]['objectHash'],
    )


@given('Assertion metaHashes as {}')
@ghernik_vars
def step(context, save_as):
    setattr(
        context,
        save_as,
        context.assertion_data['objects'][0]['metaHashes'],
    )


@given('Assertion ACL as {}')
@ghernik_vars
def step(context, save_as):
    setattr(context, save_as, context.assertion_data['ACL']) 


@when('we get the key from ACL as {}')
@ghernik_vars
def step(context, save_as):
    for acl in context.assertion_acl:
        if acl.get('reader').get('address') == context.idn_reader.address:
            key = acl.get('key')

    setattr(context, save_as, key)


@when('we decrypt {} with RSA as {}')
@ghernik_vars
def step(context, encrypted_data, save_as):
    setattr(context, save_as, context.idn_reader.decrypt(encrypted_data))


@given('Assertion message as {}')
@ghernik_vars
def step(context, save_as):
    setattr(context, save_as, context.assertion_data['message']) 

@given('Assertion metaType as {}')
@ghernik_vars
def step(context, save_as):
    setattr(
        context,
        save_as,
        context.assertion_message_body[b'assertions'][0][b'metas'][0][b'metaType'].decode()
    )


@given('Assertion metaValue as {}')
@ghernik_vars
def step(context, save_as):
    setattr(
        context,
        save_as,
        context.assertion_message_body[b'assertions'][0][b'metas'][0][b'metaValue'].decode()
    )


@given('Assertion metaSalt as {}')
@ghernik_vars
def step(context, save_as):
    setattr(
        context,
        save_as,
        context.assertion_message_body[b'assertions'][0][b'metas'][0][b'metaSalt']
    )


@given('Assertion bodyHash as {}')
@ghernik_vars
def step(context, save_as):
    setattr(context, save_as, context.assertion_data['bodyHash'])


@given('Attestation type Message_Analysis as {}')
@ghernik_vars
def step(context, save_as):
    setattr(context, save_as, 1)


@then('we sign packed_attestation_detail as {}')
@ghernik_vars
def step(context, save_as):
    attestation_sign = context.idn_sender.sign_bytes(
        context.packed_attestation_detail,
        context.client,
    )

    setattr(context, save_as, attestation_sign)


@given('Sender address as {}')
@ghernik_vars
def step(context, save_as):
    setattr(context, save_as, context.idn_sender.address)


@given('signature timestamped of {} as {}')
@ghernik_vars
def step(context, to_sign, save_as):
    signature = context.idn_sender.sign_message(to_sign, context.client)
    setattr(context, save_as, signature)


@given('Reader address as {}')
@ghernik_vars
def step(context, save_as):
    setattr(context, save_as, context.idn_reader.address)


@given('Reader public key as {}')
@ghernik_vars
def step(context, save_as):
    setattr(context, save_as, context.idn_reader.pubkey)


@given('Sender private key as {}')
@ghernik_vars
def step(context, save_as):
    setattr(context, save_as, context.idn_sender.privkey)
