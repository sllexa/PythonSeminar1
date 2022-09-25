# задача 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
from turtle import right


def input_numbers(num):
    letters = ["X", "Y", "Z"]
    numbers = []
    for i in range(num):
        numbers.append(int(input(f"Введите значение {letters[i]}: ")))
    return numbers

def check_predicate(value):
    leftValue = not value[0] or value[1] or value[2]
    rightValue = not value[0] and not value[1] and not value[2]
    return leftValue == rightValue


statement = input_numbers(3)
if check_predicate(statement):
    print("Утверждение истинно")
else:
    print("Утверждение ложно")