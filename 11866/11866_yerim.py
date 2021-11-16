import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
nums = deque(range(1, n+1))
result = []

while nums:
    for i in range(k-1):
        nums.append(nums.popleft())
    result.append(nums.popleft())

a = result[1:-1]
print('<' + a + '>')