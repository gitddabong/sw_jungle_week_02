import sys

input = sys.stdin.readline
n, c = map(int, input().split())
houses = []
for i in range(n):
    houses.append(int(input().split()))

houses.sort()


