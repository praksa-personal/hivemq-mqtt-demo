import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))

# create the client
client = mqtt.Client()
client.on_connect = on_connect

# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set("NewUser", "NewUser1234")

# connect to HiveMQ Cloud on port 8883
client.connect("874b51c1e4f04dc9838ed3d9289a3600.s1.eu.hivemq.cloud", 8883)

# subscribe to the topic "my/test/topic"
client.subscribe("my/test/topic")

# publish "Hello" to the topic "my/test/topic"
client.publish("my/test/topic", "Hello1")
client.publish("my/test/topic", "Hello2")
client.publish("my/test/topic", "Hello3")
client.publish("my/test/topic", "Hello4")

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()