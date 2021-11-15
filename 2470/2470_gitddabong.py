# # 재귀

import sys
sys.setrecursionlimit(10**8)

def binary_search(start, end):
    global mix_min, l1, l2
    if start >= end:
        return

    # 용액1 + 용액2의 절대값 = 특성값
    sum_abs = abs(liquids[start] + liquids[end])

    # 특성값이 0이면 더 볼 필요 없이 끝
    if sum_abs == 0:
        mix_min = sum_abs
        l1 = liquids[start]
        l2 = liquids[end]
        return

    # 특성값이 더 작은 페어를 찾았다면 변수에 저장
    if mix_min > sum_abs:
        mix_min = sum_abs
        l1 = liquids[start]
        l2 = liquids[end]
    
    # 특성값을 낮추려면 절대값 자체가 작아야 한다.
    # 용액1의 절대값이 크면 다음 이진탐색에서 start += 1
    if abs(liquids[start]) >= abs(liquids[end]):
        start += 1
    else:
        end -= 1
    
    binary_search(start, end)

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    liquids = list(map(int, input().split()))
    liquids.sort()
    # 혼합물 특성값의 최솟값
    mix_min = float("inf")
    # 용액1, 용액2
    l1, l2 = 0, 0

    binary_search(0, len(liquids) - 1)
    print(l1, l2)


# 반복문

# import sys
# input = sys.stdin.readline

# testcase = int(input())
# liquids = list(map(int, input().split()))
# # 정렬 후에 앞에서 뒤에서 한칸씩 움직이면서 서치할 예정
# liquids.sort()

# start = 0
# end = len(liquids) - 1

# # 특성값(두 수의 합의 절대값)의 최솟값을 저장하는 변수
# mix_min = float("inf")
# # 최솟값이 나오는 페어를 저장하는 변수 2개
# l1, l2 = 0, 0

# # start가 end와 같거나 커지면 종료
# while start < end:
#     # 두 수의 합의 절댓값
#     sum_abs = abs(liquids[start] + liquids[end])

#     # 절댓값을 구했더니 0이 나오면 종료(절댓값이 0보다 작은 수는 없으니까)
#     if sum_abs == 0:
#         l1 = liquids[start]
#         l2 = liquids[end]
#         break

#     # 특성값의 최솟값을 찾았다면 변수들 업데이트
#     if mix_min > sum_abs:
#         mix_min = sum_abs
#         l1 = liquids[start]
#         l2 = liquids[end]

#     # 보고있는 두 수의 각각의 절댓값을 구하고 절댓값이 큰쪽의 인덱스를 안쪽으로 옮기기
#     if abs(liquids[start]) > abs(liquids[end]):
#         start += 1
#     else:
#         end -= 1

# print(l1, l2)