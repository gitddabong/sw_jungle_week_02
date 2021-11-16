import sys
from collections import deque

n = int(input())
deq = deque(range(1,n+1))

i = 0 
while len(deq) > 1:
    # first phase
    if i % 2 == 0:
        deq.popleft()

    # second phase
    else:
        deq.append(deq.popleft())

    i += 1

print(deq[0])