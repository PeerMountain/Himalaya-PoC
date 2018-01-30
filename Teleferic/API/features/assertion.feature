Feature: Assertion message
    The assertion in the example is send by 4096_registred.private to 4096_a.

    @assertion
    Scenario Outline: We receive a message from a client
      Given sender Identity as sender
        And reader Identity as reader
        And Teleferic url as <teleferic_url>
        And valid_until date as <valid_until>
        And retain_until date as <retain_until>
        And object as <object>
        And metas using <meta_keys> and <meta_values>
        And container_hash as <container_hash>
        And container_key as <container_key>
        And object_hash as <object_hash>
        And result as <result>
      When we build the assertion list
        And we build the salted meta hash list using <meta_salt>
        And we build the container list
        And we build the message body
        And we build the message content with <message_key>
        And we build the message
        And we build the query
        And we send the assertion to Teleferic
      Then the query response is equal to result
      Then we check if the sender is registered
      Then we check if the reader is registered
      Then we check if the message timestamp was signed by Teleferic
        
      Examples:
      | description | teleferic_url                   | valid_until                      | retain_until                  | object    | meta_keys | meta_values | container_key                     | meta_salt                                                                                                               | message_key  | result  |
      |             | http://localhost:8000/teleferic | 2018-01-29T11:26:23.672958+00:00 | 2018-01-30:26:23.672958+00:00 | 010203    | 2         | Pepe Sarasa | validrQr3junX5yJFah16Vw89lThV9AA  | 74:26:13:2f:4d:f3:f8:3e:82:ba:f3:fe:6a:dd:46:c2:00:4c:99:e8:88:ed:0f:a9:58:85:a2:11:9e:c8:b7:46:e4:f4:f0:c3:70:30:0e:17 | test_message | success |
      |             | http://localhost:8000/teleferic | 2018-01-29T11:26:23.672958+00:00 | 2018-01-30:26:23.672958+00:00 | my_object | 2         | Pepe Sarasa | validrQr3junX5yJFah16Vw89lThV9AA  | 74:26:13:2f:4d:f3:f8:3e:82:ba:f3:fe:6a:dd:46:c2:00:4c:99:e8:88:ed:0f:a9:58:85:a2:11:9e:c8:b7:46:e4:f4:f0:c3:70:30:0e:17 | test_message | success |
