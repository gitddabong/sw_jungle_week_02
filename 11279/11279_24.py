## 11279 24 최대 힙 (시간초과)

from typing import MutableSequence
import sys


def heap_sort(a: MutableSequence) -> None:
    ## 힙 정렬
    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        ## a[left] ~ a[right] 를 힙으로 만들기
        temp = a[left]
        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1
            cr = cl + 1
            child = cr if cr <= right and a[cr] > a[cl] else cl
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)

    for i in range((n-1)//2, -1, -1):
        down_heap(a, i, n-1)

    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i-1)

if __name__ == '__main__':
    data = []
    n = int(sys.stdin.readline())
    for i in range(n):
        x = int(sys.stdin.readline().strip())
        if x == 0:
            print(0 if data == [] else data.pop())
        else:
            data.append(x)
            heap_sort(data)