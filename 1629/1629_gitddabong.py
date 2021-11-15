import sys
import math

def squared(a, size):
    # 지수가 0일 경우 1을, 지수가 1일 경우에는 a를 리턴
    # 지수가 0일 경우가 필요 없지않나? 라고 생각했었는데 
    # 진짜 필요없다
    # 지수가 0이 되려면 지수가 1인 상태에서 홀수인 경우로 들어가야 되는데
    # 그전에 size == 1 에서 걸린다
    if size == 1:
        return a

    # 지수가 짝수인 경우
    if size % 2 == 0:
        half = squared(a, size // 2)
        half %= c
        return (half * half) % c

    # 지수가 홀수인 경우
    else:
        return squared(a, size - 1) * a

if __name__ == "__main__":
    input = sys.stdin.readline

    a, b, c = map(int, input().split())
    print(squared(a, b) % c)