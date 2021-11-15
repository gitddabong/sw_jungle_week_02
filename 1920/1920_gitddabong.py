import sys
input = sys.stdin.readline

def binary_search(search_num, start, end):
    # start == end이면 다 뒤져봤다는 뜻
    if start >= end:
        if a_list[start] == b:
            print(1)
            return
        else:
            print(0)
            return

    half = (start + end) // 2
    # 인덱스 중앙값보다 비교하려는 값이 작은 경우 
    if a_list[half] > b:
        end = half - 1      # 왼쪽 파티션에 있다는 것을 확인했으니 오른쪽 파티션에 있을 수가 없으므로 왼쪽 파티션의 범위를 넣어주기 위함
        binary_search(search_num, start, end)
    # 인덱스 중앙값보다 비교하려는 값이 큰 경우
    elif a_list[half] < b:
        start = half + 1
        binary_search(search_num, start, end)
    # 어머 찾아부럿넹
    else:
        print(1)


if __name__ == "__main__":
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort()

    m = int(input())
    b_list = list(map(int, input().split()))

    # 이분 탐색
    # 정렬된 리스트의 중간 인덱스로 가서 값을 확인하고
    # 만약 그 값이 비교하려는 값보다 크면 왼쪽으로, 아니면 오른쪽으로 이동

    start = 0
    end = len(a_list) - 1

    for b in b_list:
        binary_search(b, start, end)