import paho.mqtt.client as paho
import time

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
 

client = paho.Client(client_id="Test-station-2", clean_session=True, userdata=None, protocol=paho.MQTTv31)
client.on_publish = on_publish
client.connect(host="localhost", port=1883)
client.loop_start()

data = 57

while True:
    data += 1
    msg = "Test failed. Test id: " + str(data) + "HQE"
    (rc, mid) = client.publish("testing/failed", str(msg), qos=1)
    time.sleep(5)