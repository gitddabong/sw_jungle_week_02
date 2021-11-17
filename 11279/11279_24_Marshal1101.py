## 11278 24 최대 힙 (내장 모듈 import heapq)

## heapq 모듈은 기본적으로 최소 힙처럼 적용(인덱스0에 최소값)

import sys
import heapq
from typing import MutableSequence

n = int(sys.stdin.readline())

heap_data = []
for i in range(n):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        print(0 if heap_data == [] else heapq.heappop(heap_data)[1])
    else:
        heapq.heappush(heap_data, (-x, x))

## 최대 힙으로 하려면 튜플 (-x, x)형태로 푸시하고 팝에서 인덱스1의 값 꺼내기