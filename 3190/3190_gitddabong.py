import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
apples = []
for _ in range(k):
    apples.append(list(map(int, input().split())))

l = int(input())
