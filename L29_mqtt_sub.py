import paho.mqtt.client as mqtt
import time

# callback för on_connect
def client_on_connect(client, data, flags, return_code):
    if return_code == 1:
        print("det sprack :(")
    else:
        print("connected :) hurra!")
        mySubscriber.subscribe(topic='yrgo_ei22/temp/gr1', qos=1)
    return

# callback för on_message
def client_on_message(client, data, message):
    s = message.payload.decode("utf-8")
    print(str(message.topic) + s)
    return

# callback för disconnect
def client_on_disconnect(client, userdata, rc):
    print("disconnetcted!")
    return
    
mySubscriber = mqtt.Client()
mySubscriber.on_connect = client_on_connect
mySubscriber.on_message = client_on_message
mySubscriber.on_disconnect = client_on_disconnect

mySubscriber.connect(host="broker.hivemq.com", port=1883)
mySubscriber.loop_start()

while True:
    time.sleep(1)
