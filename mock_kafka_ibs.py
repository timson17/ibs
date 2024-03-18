from flask import Flask, request, jsonify  # импортируем необходимые модули из фласк
from kafka import KafkaProducer  # импортируем необходимые модули из кафка
import json  # импортируем жсон

app = Flask(__name__)  # создаем экземпляр фласк
app.debug = True  # включен дебаг

# создаем кафка продюсер указываем айпи кафка и сериализатор
producer = KafkaProducer(bootstrap_servers='172.20.10.2:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


@app.route('/test', methods=['POST'])  # определение маршрута и метода
def process_data():
    data = request.get_json()  # функция для обработки запроса

    # Обрабатываем данные (меняем возраст на 96)
    # data['age'] = 96

    def replace_age(dictionary, new_age):  # рекурсивная функция для замены значений ключа age
        for key, value in dictionary.items(): # проходим по всем элементам словаря
            if key == 'age': # если ключ age то значение = new_age
                dictionary[key] = new_age
            elif isinstance(value, dict): # проверяем является ли значение словарем
                replace_age(value, new_age) # если элемент списка словарь вызывается рекурсивно функция replace_age для этого словаря.
            elif isinstance(value, list): # если значение является списком то проходимся по элементам списка
                for item in value:
                    if isinstance(item, dict):
                        replace_age(item, new_age)

    new_age = 96  # переменная со значением 96 на которое меняем по значения по ключу age
    replace_age(data, new_age)  # вызываем функцию изменяющую значения ключа age

    producer.send('test', value=data)  # отправляем обработанные данные в Kafka в топик test
    print(data)  # выводим на экран измененный json

    return jsonify({"message": "Данные обработаны и отправлены в kafka"})  # функция replace_age возвращает json ответ


if __name__ == '__main__':  # точка входа фласк приложения с портом 5000
    app.run(port=5000)
