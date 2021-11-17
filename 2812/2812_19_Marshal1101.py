## 2812 19 크게 만들기 (참조)

import sys

n, k = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().strip()))

result = []     #최종 만들 숫자가 담길 리스트
delNum = k      #숫자를 지울 횟수 = 몇 번 pop하는가

for i in range(n):
    while delNum > 0 and result:
        if result[len(result)-1] < data[i]:
            result.pop()
            delNum-=1
        else:
            break
    result.append(data[i])
    
for i in range(n-k):
    print(result[i], end="")