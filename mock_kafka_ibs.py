from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json

app = Flask(__name__)
app.debug = True

# Создаем Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


@app.route('/test', methods=['POST'])
def process_data():
    data = request.get_json()
    # Обрабатываем данные (меняем возраст на 96)
    data['age'] = 96


    # Отправляем обработанные данные в Kafka
    producer.send('test', value=data)
    print(data)

    return jsonify({"message": "Data processed and sent to Kafka"})


if __name__ == '__main__':
    app.run(port=5000)