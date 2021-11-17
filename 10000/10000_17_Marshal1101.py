import sys

n = int(sys.stdin.readline())
data = []
for i in range(n):
    x, r = list(map(int,sys.stdin.readline().split()))
    data.append([0, x-r])
    data.append([1, x+r])

data.sort(reverse=True)
data.sort(key=lambda x: x[1])

print(data)

stk = [None] * n * 2
ptr = 0
no = 0

def push(value):
    global ptr
    global no
    stk[ptr] = value
    ptr += 1
    no += 1

def pop():
    global ptr
    global no
    ptr -= 1
    x = stk[ptr]
    no -= 1
    return x

def peek():
    global ptr
    x = stk[ptr-1]
    return x

def find(value):
    for i in range(ptr-1, -1, -1):
        if stk[i][0] == value:
            return i
    return -1

count = 1
max_d = 0
push(data[0])
for i in range(1, 2*n):
    if peek()[0] == 0 and data[i][0] == 0:
        push(data[i])
    elif peek()[0] == 0 and data[i][0] == 1:
        d = data[i][1] - pop()[1]
        push([3, d])
        max_d += d
    else:
        if data[i][0] == 0:
            push(data[i])
        elif data[i][0] == 1:
            if find(0):
                k = ptr - find(0)
                for _ in range(k-1):
                    pop()
                    count += 1
                if ptr == 1:
                    D = data[i][1] + pop()[1]
                    push([3, D])
                    if max_d == D:
                        count += 2
                else:
                    d = data[i][1] + pop()[1]
                    push([3, d])
                    max_d += d
    

print(n + count)
