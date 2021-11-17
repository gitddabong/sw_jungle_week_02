# 2110 03 공유기 설치 (답안)

import sys

n, c = map(int,sys.stdin.readline().split())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline().strip()))

data.sort


## start 최소, end 최대
start = 1
end = data[-1] - data[0]
answer = 0

def binary_search(data, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = data[0]
        count = 1

        for i in range(1, len(data)):
            if data[i] >= current + mid:
                count += 1
                current = data[i]

        if count >= c:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1


binary_search(data, start, end)
print(answer)