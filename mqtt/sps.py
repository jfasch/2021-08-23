from paho.mqtt import client
import json
import datetime


c = client.Client()
c.connect('localhost')

now = datetime.datetime.now()

msg = {
    'timestamp': now.timestamp(),
    'text': 'seas oida',
}

msg_payload = json.dumps(msg)
c.publish('/spsen/meine-sps', msg_payload)
