# 10830 10 행렬 제곱 (시간초과)

from __future__ import annotations
import sys

n, b = map(int,sys.stdin.readline().split())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
c = 1000

def matrix_expo(n, matrix):
    result = [[0 for _ in range(n)] for _ in range(n)]
    temp = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix[i][k] * matrix[k][j]
    return result

def matrix_time(n, matrix1, matrix2):
    result = [[0 for _ in range(n)] for _ in range(n)]
    temp = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def divide_expo(n, b, matrix):
    if b == 1:
        return matrix
    elif b == 2:
        return matrix_expo(n, matrix)
    else:
        temp = divide_expo(n, b//2, matrix)
        if b % 2 == 0:
            return matrix_expo(n, temp)
        else:
            return matrix_time(n, matrix, matrix_expo(n, temp))

ans = divide_expo(n, b, matrix)
for row in ans:
    for num in row:
        print(num % c, end=' ')
    print()
