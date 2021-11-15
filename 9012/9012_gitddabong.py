# 출력이 no가 되는 조건은 총 2가지다.
# 1. 괄호를 열어만 놓고 마저 안 닫는 경우
# 2. 괄호가 없는데 닫으려고 하는 경우

import sys
from collections import deque

input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase):
    strings = list(input())

    deq = deque()
    no_flag = False     # 괄호가 없는데 닫으려고 하는 경우를 저장하는 flag

    for string in strings:
        if string == "(":
            deq.append(string)
        elif string == ")":
            # 길이가 0이 아니다 = 스택에 괄호가 들어있다
            if len(deq) != 0:
                deq.pop()
            else:
                no_flag = True
                break
    
    # 1번 케이스 및 2번 케이스인 경우
    if len(deq) != 0 or no_flag == True:
        print("NO")
    else:
        print("YES")