# temp와 result의 관계를 아직 잘 모르겠다
# 손으로 직접 계산할 때는 2*11 + 2*3 = 28인데
# 여기서 계산하면 4+18 + 2*3 = 28
# 왜??
# 큰 괄호 안에 있으면 괄호안 계산값 *2 인데
# 이 코드에서는 2*2 + 9*2 즉, 분배법칙으로 구현
# ㅁㅊ 어케생각했노

import sys
from collections import deque
input = sys.stdin.readline

strings = list(input())
deq = deque()

temp = 1
result =  0
wrong_flag = False

for i in range(len(strings)):
    # 괄호가 시작되면 temp에 *2
    if strings[i] == '(':
        temp *= 2
        deq.append('(')

    # 대괄호가 시작되면 temp에 *3
    elif strings[i] == '[':
        temp *= 3
        deq.append('[')

    # 괄호가 끝남
    elif strings[i] == ')':
        # 리스트에 남은 괄호가 없거나 스택에 남은 마지막 괄호가 짝이 안맞을 경우 잘못된 입력
        if len(deq) == 0 or deq[-1] != '(':
            wrong_flag = True
            break

        # 직전 괄호가 짝이 맞으면 temp를 result에 추가
        if strings[i - 1] == '(':
            result += temp
        deq.pop()
        temp //= 2

    elif strings[i] == ']':
        if len(deq) == 0 or deq[-1] != '[':
            wrong_flag = True
            break

        if strings[i - 1] == '[':
            result += temp
        deq.pop()
        temp //= 3

if wrong_flag == True or len(deq) != 0:
    print(0)
else:
    print(result)
