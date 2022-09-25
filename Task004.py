# задача 4 HARD необязательная Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.
def calculation():
    if action == "/" or action == "mod" or action == "div":
        if second_number == 0:
            print("Деление на 0!")
            exit()
    result = None
    if action == "+":
        result = first_number + second_number
    elif action == "-":
        result = first_number - second_number
    elif action == "*":
        result = first_number * second_number
    elif action == "/":
        result = first_number / second_number
    elif action == "mod":
        result = first_number % second_number
    elif action == "pow":
        result = first_number ** second_number
    elif action == "div":
        result = first_number // second_number
    return result


first_number = float(input("Введите число 1: "))
second_number = float(input("Введите число 2: "))
action = input("Введите действие: ")
print(calculation())

