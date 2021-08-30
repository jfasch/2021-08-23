from paho.mqtt import client
import json
import datetime
import time
import random
import uuid
from collections import namedtuple


Message = namedtuple('Message', ('msgid', 'timestamp', 'message'))
def make_message(text):
    return Message(message=text, msgid=uuid.uuid4().fields, timestamp=time.time())

class MQTTBrokerClient:
    def __init__(self, host, port, topic):
        self.client = client.Client()
        self.client.connect(host, port)
        self.topic = topic
    def send_message(self, message):
        msg = {'message': message.message,
               'msgid': message.msgid,
               'timestamp': message.timestamp }
        self.client.publish(self.topic, json.dumps(msg))

# class UPCUABrokerClient:
#     def __init__(self, blah):
#         self.blah = blah
#     def send_message(self, msgid, message):
#         # ...

class ErrorHandler:
    def __init__(self, brokerclient):
        self.log = []
        self.brokerclient = brokerclient
    def shit_happened(self, shit):
        m = make_message(shit)
        self.log.append(m)
        self.brokerclient.send_message(m)

c = MQTTBrokerClient('localhost', 1883, '/spsen/meine-sps')
# c = UPCUABrokerClient('blah')

errorhandler = ErrorHandler(c)

while True:
    bullshit = 'bullshit ' + str(random.randrange(1000))
    errorhandler.shit_happened(bullshit)
    time.sleep(1.2)
