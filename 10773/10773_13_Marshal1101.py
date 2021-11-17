# 10773 13 제로 (완료)

import sys

k = int(sys.stdin.readline())
num_list = []
for _ in range(k):
    num_list.append(int(sys.stdin.readline()))

stk = [None] * 100000
ptr = 0

def empty():
    global ptr
    if ptr <= 0:
        return 1
    else:
        return 0

def push(value):
    global ptr
    stk[ptr] = value
    ptr += 1

def pop():
    global ptr
    if empty():
        return -1
    ptr -= 1
    return stk[ptr]

def delete():
    global ptr
    if empty():
        return -1
    ptr -= 1
    stk[ptr] = None

def size():
    global ptr
    return ptr

def top():
    global ptr
    if stk[ptr-1] != None:
        return stk[ptr-1]
    else:
        return -1

def dump():
    return stk[:ptr]

for num in num_list:
    if num == 0:
        delete()
    else:
        push(num)

total = 0
for i in dump():
    total += i

print(total)