import sys

def tree_cut(height):
    sum = 0
    for tree in trees:
        if tree >= height:
            sum += tree - height

    return sum

def binary_search(start, end):
    global cost_min, length_max
    # 다 뒤져봤다
    # start >= end 하면 안됨.
    # 그러면 start == end (half = start+end / 2) 인 경우를 확인하지 않고 함수를 종료해버림
    if start > end:
        return

    # start와 end를 이용해 반값을 구하고 얘를 기준으로 나무자르기
    half = int((start + end) / 2)
    cost_sum = tree_cut(half)
    # 합계를 지금까지의 나무 길이의 최솟값과 비교해서 더 작으면 넣기
    # 나무 길이의 합계가 현재까지 나온 합계 중 최솟값이라면 
    # 합계 최솟값 업데이트, 나무 길이 최댓값 업데이트
    if cost_sum >= target and cost_min > cost_sum:
        cost_min = cost_sum
        length_max = half

    # 목표치보다 합계가 높으면 높이를 더 올려서 재검색
    if target <= cost_sum:
        start = half + 1
    else:
        end = half - 1

    binary_search(start, end)

if __name__ == "__main__":
    input = sys.stdin.readline

    n, target = map(int, input().split())
    trees = list(map(int, input().split()))

    cost_min = float("inf")
    length_max = 0

    # 높이의 시작과 끝을 0과 제일 긴 나무의 길이로 설정
    binary_search(0, max(trees))

    print(length_max)