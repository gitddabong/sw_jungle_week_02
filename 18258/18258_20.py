## 18258 20 큐 2 (참조, 내장함수 deque)

import sys
from collections import deque
 
n = int(input())
q = deque()
 
for _ in range(n):
    cmd = list(map(str, sys.stdin.readline().split()))
    if cmd[0] == 'push':
        q.append(cmd[1])
    elif cmd[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print("-1")
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if q:
            print(q[0])
        else:
            print("-1")
    elif cmd[0] == 'back':
        if q:
            print(q[-1])
        else:
            print("-1")


## 18258 20 큐 2 (deaue 없이)
# from sys import stdin
# input()
# s, com= [], stdin.readlines()
# cnt = 0
# for x in com:
#     c = x.split()
#     if c[0] == "push":
#         s.append(c[1])
#     elif c[0] == 'pop':
#         if len(s) > cnt:
#             print(s[cnt])
#             cnt += 1
#         else: print(-1)
#     elif c[0] == 'size':
#         print(len(s)-cnt)
#     elif c[0] == 'empty':
#         if len(s) == cnt :
#             print(1)
#             cnt = 0
#             s = []
#         else: print(0)
#     elif c[0] == 'front':
#         if len(s) > cnt: print(s[cnt])
#         else: print(-1)
#     elif c[0] == 'back':
#         if len(s) > cnt: print(s[-1])
#         else: print(-1)