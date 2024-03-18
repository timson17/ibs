from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('test', bootstrap_servers='172.20.10.2:9092')

for message in consumer:
    message_value = message.value.decode('utf-8')
    data = json.loads(message_value)
    print (data)