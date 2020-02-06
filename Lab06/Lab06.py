# 3
# 1) Дан одномерный массив А длиной М<=20, упорядоченный по убыванию.
# - переупорядочить массив А по возрастанию его элементов, используя первоначальную упорядоченность массива.
# 2) Дана действительная квадратная матрица порядка N=12.
# - найти сумму элементов, расположенных на побочной диагонали и выше ее;

import pickle
from random import random

print("Переупорядочить массив:")
desc_list = []

for i in range(20, 0, -1):
    desc_list.append(i)
print(desc_list)

print("Запись массива в файл")
with open('desc_list.pickle', 'wb') as f:
    pickle.dump(desc_list, f)

print("Чтение массива из файла")
with open('desc_list.pickle', 'rb') as f:
    desc_list_new = pickle.load(f)

asc_list = desc_list_new[::-1]
print(asc_list)

print()

print("Найти сумму элементов, расположенных на побочной диагонали матрицы N=12 и выше ее")

N = 12
matrix = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(int(random()*10))
    matrix.append(row)

print("Запись матрицы в файл")
with open('matrix.pickle', 'wb') as f:
    pickle.dump(matrix, f)

print("Чтение матрицы из файла")
with open('matrix.pickle', 'rb') as f:
    matrix_new = pickle.load(f)

for row in matrix_new:
    print(row)

sumSecondaryAndAbove = 0
for i in range(N):
    k = N - i
    for j in range(k):
        sumSecondaryAndAbove += matrix_new[i][j]

print(sumSecondaryAndAbove)
