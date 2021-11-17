# 1920 01 수 찾기 (완료)
from typing import Any, Sequence
import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))
a.sort()


def bin_search(a: Sequence, b: Sequence) -> Sequence:

    result = []
    for key in b:
        pl = 0
        pr = n - 1
        while True:
            pc = (pl + pr) // 2
            if a[pc] == key:
                result.append(1)
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                result.append(0)
                break
    return result
result = bin_search(a, b)
for i in result:
    print(i)









# # 선형검색 시간초과

# from typing import Any, Sequence
# import sys

# n = int(sys.stdin.readline())
# a = list(map(int,sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# b = list(map(int,sys.stdin.readline().split()))

# def seq_search(a: Sequence, b: Sequence) -> Sequence:
#     result = []
#     for j in b:
#         if j in a:
#             result.append(1)
#         else:
#             result.append(0)
#     return result

# seq_search(a, b)