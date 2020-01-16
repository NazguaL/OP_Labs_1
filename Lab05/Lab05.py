# Создать Windows Forms - приложение:
# • форма должна содержать поле для ввода значения переменной x;
# • результат вычислений отобразить на форме;

import math

users_input = input("Введите значение целое число: ")

try:
    x = float(users_input)
    print("Вы ввели число: ", x)
except ValueError:
    print("Введенное вами значение не число!")


a = math.log1p(math.sqrt((math.exp(x + 1) + 2 * math.exp(x) * math.cos(x))))
b = math.log1p(x - math.exp(x + 1) * math.sin(x))
c = math.fabs(math.cos(x)/math.exp(math.sin(x)))
z = 6 * a/b * c
print(z)
