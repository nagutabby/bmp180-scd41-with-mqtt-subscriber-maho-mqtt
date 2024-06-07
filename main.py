from paho.mqtt import client as mqtt

TOPIC_PREFIX = 'i483/sensors/s2410064'
BROKER = '150.65.230.59'

topics = [
    f'{TOPIC_PREFIX}/SCD41/co2',
    f'{TOPIC_PREFIX}/SCD41/humidity',
    f'{TOPIC_PREFIX}/SCD41/temperature',
    f'{TOPIC_PREFIX}/BMP180/temperature',
    f'{TOPIC_PREFIX}/BMP180/air_pressure'
]

def on_connect(client, userdata, flags, reason_code, properties):
        print(f'Connected with result code {reason_code}')
        for topic in topics:
            client.subscribe(topic)


def on_message(client, userdata, message):
    print(f'{message.topic}: {message.payload.decode()}')

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(BROKER)

mqtt_client.loop_forever()
