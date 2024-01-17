import paho.mqtt.client as mqtt
import time

# Enligt dokumentation https://pypi.org/project/paho-mqtt/#callbacks
def client_on_connect(client, data, flags, return_code):
    if return_code == 1:
        print('Could not connect \n')
    else:
        print('Connect ed successfully! \n')
    return 

client1 = mqtt.Client()
client1.on_connect = client_on_connect #knyt en callback
client1.connect(host='broker.hivemq.com', port=1883)

client1.loop_start()

temp = 20.1

while True:
    temp += 1
    msg = client1.publish(topic='yrgo_ei22/temp/gr1', payload=str(temp), qos=1) #qos 1 - kräv ack
    msg.wait_for_publish()
    time.sleep(5)
    print('.')

