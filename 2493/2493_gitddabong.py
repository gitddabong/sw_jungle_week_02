import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))
deq = deque()

for i in range(n):
    while(len(deq) > 0):
        # 스택의 top이 현재 입력값보다 크다면 신호 수신 가능이므로
        if(deq[-1][1] > towers[i]):
            # top의 위치를 출력하고 반복문을 탈출한다
            print(deq[-1][0], end=" ")
            break

        deq.pop()
    
    if len(deq) == 0:
        print(0, end=" ")
    deq.append([i+1, towers[i]])








# deq = deque()
# deq.append(towers[0])

# for i in range(1, n):
#     # deq 안에 있는 탑의 길이가 현재 탑의 길이보다 크면 더 이상 필요없으므로 pop하고 현재 탑의 길이를 push
#     if deq[len(deq) - 1] < towers[i]:
#         deq.pop()
#         deq.append(towers[i])
#     # 현재 탑의 길이가 작으면 다음 탑의 길이가 얘보다 더 작을 수도 있으니 push
#     else:
#         deq.append(towers[i])





# deq = deque(map(int, input().split()))

# # 지금까지 최고점이었던 인덱스와 높이의 최댓값 저장
# max_index = n-1
# height_max = deq.pop()

# # 출력값을 저장하는 리스트
# checklist = [0] * n

# # 누적된 탑의 개수를 저장하는 카운트(위에서 첫 값 하나 지웠으니까 카운트 + 1)
# count = 1

# # 뒤에서부터 pop하면서 출력값 리스트에 값 저장
# for i in range(len(deq) - 1, -1, -1):
#     height_now = deq.pop()

#     # 새로받은 값이 높이가 더 높은 경우
#     if height_max <= height_now:
#         height_max = height_now
        
#         # 이전까지의 인덱스에 현재 위치의 인덱스 + 1 저장
#         for j in range(i+1, i+1 + count):
#             checklist[j] = i+1

#         count = 1

#     else:
#         count += 1

# for check in checklist:
#     print(check, end=" ")

