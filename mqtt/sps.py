from paho.mqtt import client
import json
import datetime
import time
import random
import uuid


class ErrorHandler:
    def __init__(self, mqtt, topic):
        self.log = []
        self.sequence = 0
        self.mqtt = mqtt
        self.topic = topic
    def shit_happened(self, shit):
        msg = {'shit': shit,
               'msgid': uuid.uuid4().fields }
        self.log.append(msg)
        self.mqtt.publish(self.topic, json.dumps(msg))

c = client.Client()
c.connect('localhost')

errorhandler = ErrorHandler(c, '/spsen/meine-sps')

while True:
    bullshit = 'bullshit ' + str(random.randrange(1000))
    errorhandler.shit_happened(bullshit)
    time.sleep(1.2)
