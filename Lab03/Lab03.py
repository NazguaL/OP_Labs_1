# Задание
# Реализовать приведение типов согласно варианта:
# uint > ulong
# ushort > byte
#
# класс Convert (методы с таблицы).
# 1, 10, 20, 30 ,40

users_input = input("Введите целое число: ")

try:
   val = int(users_input)
   print("Вы ввели число: ", val)
except ValueError:
    try:
        val = float(users_input)
        print("Вы ввели число с плавающей точкой: ", val)
    except ValueError:
        print("Введенное вами значение не число!")
