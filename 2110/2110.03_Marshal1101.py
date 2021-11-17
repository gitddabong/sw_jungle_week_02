## 2110 3 공유기 설치 (완료)

import sys
input = sys.stdin.readline

n, c = map(int,input().split())
x = []
for _ in range(n):
    x.append(int(input().strip()))

x.sort()

def bsearch(list):
    dleft = 1
    dright = list[-1] - list[0]
    while dleft <= dright:
        d = (dleft + dright) // 2
        now = list[0]
        count = 1
        for i in range(1, n):
            if list[i] - now >= d:
                count += 1
                now = list[i]
        if count >= c:
            maxd = d
            dleft = d + 1
        else:
            dright = d - 1

    return maxd

print(bsearch(x))