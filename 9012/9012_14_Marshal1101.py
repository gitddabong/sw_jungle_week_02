# 9012 14 괄호 (완료)

import sys

t = int(sys.stdin.readline())
data = []
for _ in range(t):
    data.append(sys.stdin.readline().strip())

stk = [None] * 100000
ptr = 0

def push(value):
    global ptr
    stk[ptr] = value
    ptr += 1

def delete():
    global ptr
    ptr -= 1
    stk[ptr] = None


for bracket in data:
    ptr = 0
    if bracket[0] == ')':
        print('NO')
        continue
    for i in range(len(bracket)):
        if bracket[i] == '(':
            push(1)
        elif bracket[i] == ')':
            delete()
        if ptr < 0:
            break
    
    if ptr == 0:
        print('YES')
    else:
        print('NO')
