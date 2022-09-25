# Задача 5 VERY HARD SORT необязательная
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
# После сортировки
# 1 2 3 4
# 5 7 9 10
from random import randint

def output_array(array):
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            print(array[i][j], end=" ")
        print()

def create_array(row, col):
    array = [0] * row
    for i in range(row):
        array[i] = [0] * col
        for j in range(col):
            array[i][j] = randint(1, 10)
    return array

def sort_array(array):
    tmp = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            for k in range(len(array[i]) - 1):
                if array[i][k] > array[i][k + 1]:
                    tmp = array[i][k]
                    array[i][k] = array[i][k + 1]
                    array[i][k + 1] = tmp
    return array

row = int(input("Введите количество строк массива: "))
col = int(input("Введите количество столбцов массива: "))

array_number = create_array(row, col)
output_array(array_number)
print()
array_new = sort_array(array_number)
output_array(array_new)


