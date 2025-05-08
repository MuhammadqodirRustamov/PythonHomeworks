import random

import numpy
from numpy.matrixlib.defmatrix import matrix

# 1
# vector = numpy.arange(10, 50)
# print(vector)

# 2
# matrix = numpy.arange(0, 9).reshape(3, 3)

# 3
# _list = [1, 0, 0, 0, 1, 0, 0, 0, 1]
# matrix = numpy.array(_list).reshape(3, 3)

# 4
# _list = [random.randint(0,100) for _ in range(27)]
# matrix = numpy.array(_list).reshape(3,3,3)

# 5
# _list = [random.randint(0, 1000) for _ in range(0, 100)]
# matrix = numpy.array(_list).reshape(10,10)
# print(f"Max = {matrix.max()}")
# print(f"Min = {matrix.min()}")

# 6
# vector = numpy.array([random.randint(0,100) for _ in range(30)])
# print(vector.mean())

# 7
# _list = [random.randint(0,100) for _ in range(25)]
# matrix = numpy.array(_list).reshape(5,5)
# matrix = matrix / matrix.max()

# 8
# _list1 = [random.randint(0, 10) for _ in range(15)]
# _list2 = [random.randint(0, 10) for _ in range(6)]
#
# matrix1 = numpy.array(_list1).reshape(5, 3)
# matrix2 = numpy.array(_list2).reshape(3, 2)
# print(numpy.dot(matrix1, matrix2))

# matrix = matrix1 * matrix2

# 9
# _list1 = [random.randint(0, 10) for _ in range(9)]
# _list2 = [random.randint(0, 10) for _ in range(9)]
#
# matrix1 = numpy.array(_list1).reshape(3, 3)
# matrix2 = numpy.array(_list2).reshape(3, 3)
# print(matrix1)
# print(matrix2)
# matrix = matrix1 * matrix2

# 10
# _list = [random.randint(0,100) for _ in range(16)]
# matrix = numpy.array(_list).reshape(4,4)
# print(matrix)
# print(matrix.T)

# 11
# _list = [random.randint(0, 10) for _ in range(9)]
# matrix = numpy.array(_list).reshape(3, 3)
# print(matrix)
# print(numpy.linalg.det(matrix))

# 12
# _list1 = [random.randint(0, 10) for _ in range(12)]
# _list2 = [random.randint(0, 10) for _ in range(12)]
#
# matrix1 = numpy.array(_list1).reshape(3, 4)
# matrix2 = numpy.array(_list2).reshape(4, 3)
#
# print(numpy.dot(matrix1, matrix2))

# 13

# _list1 = [random.randint(0, 10) for _ in range(9)]
# _list2 = [random.randint(0, 10) for _ in range(3)]
#
# matrix1 = numpy.array(_list1).reshape(3, 3)
# matrix2 = numpy.array(_list2)
# print(matrix1)
# print(matrix2)
# print(matrix1 * matrix2)

# 14

# _list1 = [random.randint(0, 10) for _ in range(9)]
# _list2 = [random.randint(0, 10) for _ in range(3)]
#
# matrix = numpy.array(_list1).reshape(3, 3)
# vector = numpy.array(_list2)
#
# det_m = numpy.linalg.det(matrix)
#
# if det_m != 0:
#     # Compute the inverse of A
#     m_inv = numpy.linalg.inv(matrix)
#
#     # Solve for x
#     x = numpy.dot(m_inv, vector)
#     print("Solution x:", x)
# else:
#     print("Matrix A is singular (no unique solution).")

# 15
_list = [random.randint(0, 10) for _ in range(25)]
matrix = numpy.array(_list).reshape(5, 5)
print("Row wise: ", end="")
for row in range(0, 5):
    sum_of_row = sum(matrix[row, :])
    print(sum_of_row, end=" ")
print()
print("Column wise: ", end="")
for column in range(0, 5):
    sum = 0
    for row in range(0, 5):
        sum += matrix[row, column]
    print(sum, end=" ")
print()
print(matrix)
