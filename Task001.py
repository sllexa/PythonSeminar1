# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
def input_number(text):
    try:
        number = int(input(text))
    except:
        print('Это не число')
    return number


def check_number(number):
    if number == 6 or number == 7:
        print('Да')
    elif 0 < number < 6:
        print('Нет')
    else:
        print('Такого дня недели нет')


number = input_number('Введите число: ')
check_number(number)