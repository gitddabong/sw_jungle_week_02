## 8983 6 사냥꾼 (완료)

import sys
input = sys.stdin.readline

m, n, l = map(int,input().split())
hunters = list(map(int,input().split()))
animals = []
for _ in range(n):
    x, y = map(int,input().split())
    if y <= l:
        animals.append((x, y))

hunters.sort()
animals.sort()

idx = 0
count = 0

for i in range(len(animals)):
    left, right = idx, m-1
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        if hunters[mid] <= animals[i][0]:
            if mid+1 == m or hunters[mid+1] > animals[i][0]:
                break
            left = mid + 1
        else:
            right = mid - 1
    idx = mid
    if abs(hunters[mid] - animals[i][0]) + animals[i][1] <= l:
        count += 1
    elif m > mid+1 and abs(animals[i][0] - hunters[mid+1]) + animals[i][1] <= l:
        count += 1
print(count)


