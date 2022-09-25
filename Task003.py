# задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
def input_coordinates(num):
    coord = [0] * num
    for i in range(num):
        is_ok = False
        while not is_ok:
            try:
                coord[i] = int(input(f"Введите координату {i + 1}: "))
                is_ok = True
                if coord[i] == 0:
                    is_ok = False
                    print("Координата не должна равняться нулю")
            except:
                print("Вводить нужно целые числа")
    return coord


def check_coordinates(coord):
    quarter = 4
    if coord[0] > 0 and coord[1] > 0:
        quarter = 1
    elif coord[0] < 0 and coord[1] > 0:
        quarter = 2
    elif coord[0] < 0 and coord[1] < 0:
        quarter = 3
    return quarter


coord = input_coordinates(2)
print(f"Точка находится в {check_coordinates(coord)} четверти")
