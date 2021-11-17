# 10830 10 행렬 곱셈 함수(참조)



### 방법1 2진법 변환 분할정복
def matrix_mul(a, b):
    result = [[0]* N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += a[i][k] * b[k][j]
    
    for i in range(N):
        for j in range(N):
            result[i][j] %= 1000
                
    return result
    
    
#2진법으로 변환하여 분할정복 실행
N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
B = bin(B)[2:] #2진법으로 변환 2: <- 두 자리 수

#단위 행렬
identity_matrix = [[1 if i == j else 0 for i in range(N)] for j in range(N)]

#2진법 자릿수 만큼 제곱 & 제곱한 행렬 끼리 곱해줌
result = identity_matrix[:]
for i in range(len(B)):
    if B[-i-1] == '1':
        temp = matrix[:]
        while i != 0:
            temp = matrix_mul(temp, temp)
            i -= 1
        result = matrix_mul(result, temp)

for row in result:
    print(*row)





### 방법2 1629곱셈을 이용한 분할정복
def mul(n,matrix1,matrix2):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= 1000

    return result

# 2분할
def devide(n,b,matrix):
    if b == 1:
        return matrix
    elif b == 2:
        return mul(n,matrix,matrix)
    else:
        tmp = devide(n,b//2,matrix)
        if b%2 == 0:
            return mul(n,tmp,tmp)
        else:
            return mul(n,mul(n,tmp,tmp),matrix)

# 입력
n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

result = devide(n,b,a)
for row in result:
    for num in row:
        print(num%1000, end=' ')
    print()