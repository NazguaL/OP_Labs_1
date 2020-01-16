# 3
# 1) Дан одномерный массив А длиной М<=20, упорядоченный по убыванию.
# - переупорядочить массив А по возрастанию его элементов, используя первоначальную упорядоченность массива.
# 2) Дана действительная квадратная матрица порядка N=12.
# - найти сумму элементов, расположенных на побочной диагонали и выше ее;

print("Переупорядочить массив:")
desc_list = []
for i in range(20, 0, -1):
    desc_list.append(i)
print(desc_list)
asc_list = desc_list[::-1]
print(asc_list)

print()

print("Найти сумму элементов, расположенных на побочной диагонали матрицы N=12 и выше ее")
from random import random
N = 12
matrix = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(int(random()*10))
    matrix.append(row)

for row in matrix:
    print(row)

sumSecondaryAndAbove = 0
for i in range(N):
    k = N - i
    for j in range(k):
        sumSecondaryAndAbove += matrix[i][j]

print(sumSecondaryAndAbove)
