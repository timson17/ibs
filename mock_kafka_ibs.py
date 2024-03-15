from flask import Flask, request, jsonify
from confluent_kafka import Producer
import json


app = Flask(__name__)
producer = Producer({'bootstrap.servers': 'localhost:9092'})


def process_data(data):
    data['age'] = 96
    return data


@app.route('/process_data', methods=['POST'])
def process_rest_request():
    req_data = request.get_json()
    processed_data = process_data(req_data)

    # Отправка в kafka
    producer.produce('processed_data_topic', value=bytes(json.dumps(processed_data), encoding='utf-8'))
    producer.flush()

    return jsonify({'message': 'Data processed and sent to Kafka'})


if __name__ == '__main__':
    app.run(port=5000)
