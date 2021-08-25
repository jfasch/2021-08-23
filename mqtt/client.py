from paho.mqtt import client
import json
import datetime


c = client.Client()
c.connect('localhost')

def sps_message_received(client, userdata, msg):
    print(msg.payload)
c.on_message = sps_message_received

c.subscribe('/spsen/meine-sps')
c.loop_forever()
