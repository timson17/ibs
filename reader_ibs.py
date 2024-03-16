from kafka import KafkaConsumer

consumer = KafkaConsumer('test', bootstrap_servers='192.168.0.129:9092')

for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                        message.offset, message.key,
                                        message.value))