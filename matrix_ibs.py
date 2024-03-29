import random  # импортируем модуль рандом для заполнения массива


def create_array(n):  # объявляем функцию для создания массива и передаем в нее значение n
    return [[random.randint(1, 100) for _ in range(n)] for _ in range(
        n)]  # наполняем массив случайными числами в диапазоне от 1 до 100 и возвращаем как результат выполнения функции
    # внутренний цикл for _ in range(n) выполняется n раз в каждой строке заполняя ее случайными числами
    # внешний цикл for _ in range(n) выполняется n раз каждый раз создавая новую строку матрицы
    # _ используется когда переменная не используется внутри цикла


def find_min(matrix):  # обьявляем функцию для поиска минимума и передаем matrix
    min_element = matrix[n - 1][0]  # обьявляем минимальный элемент массива -1 так как массив начинается с 0
    for i in range(n):  # бежим по циклу n раз так как элементов по диагонали тоже n
        min_element = min(min_element, matrix[n - i - 1][i])  # ищем минимум по индексу
    return min_element  # возвращаем переменнубю min_element как результат выполнения функции


n = int(input("Введите число N которое >=3 "))  # записываем в n целочисленную переменную
if n < 3:  # если n меньше 3
    print("Число N должно быть больше или равно 3.")  # то выводим сообщение
else:  # иначе
    matrix = create_array(n)  # создаем матрицу и вызываем функцию создания массива
    print("Сгенерированный двумерный массив:")  # выводим сообщение
    for elementi in matrix:  # создаем цикл для перебора массива и вывода его на экран
        print(elementi)

    min_element = find_min(matrix)  # вызываем функцию для поиска минимального элемента по побочной диагонали
    print("Минимальный элемент на побочной диагонали:", min_element)  # выводим найденый минимальный элемент
