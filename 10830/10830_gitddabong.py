import sys

n, b = map(int, sys.stdin.readline().split())
numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 한 행렬을 제곱하는 함수
def mul_matrix(a, b):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j] 
            result[i][j] %= 1000
    
    return result

# 지수를 나누면서 부분연산을 진행하는 재귀함수
def multi(b):
    if b == 1:
        return numbers
    
    # b가 짝수면 제곱
    if b % 2 == 0:
        # return mul_matrix(multi(b // 2), multi(b // 2)) #시간초과 이유
        val = multi(b // 2) 
        return mul_matrix(val, val)
    
    # b가 홀수면 지수-1 하고 입력받은 행렬 한번 곱해주기 (A^3 = A^2 * A)
    else:
        return mul_matrix(multi(b - 1), numbers)
    
result_matrix = multi(b)
    
for row in result_matrix:
    for col in row:
        print(col % 1000, end=" ")
    print()