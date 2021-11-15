# 입력받는것마다 스택에 다 집어넣고 
# 맨 앞에것을 최댓값으로 설정하고 (카운트 + 1)
# 빼면서 최댓값보다 더 큰 수가 있으면 최댓값을 갱신하고 카운트 + 1

import sys
from collections import deque

input = sys.stdin.readline

deq = deque()
n = int(input())
for _ in range(n):
    deq.append(int(input()))

stick_max = 0
cnt = 0

for i in range(n):
    stick_len = deq.pop()
    if stick_max < stick_len:
        stick_max = stick_len
        cnt += 1

print(cnt)