# 6549 9 히스토그램에서 가장 큰 직사각형(참조)

# 방법1 단순코딩 (시간초과)
def solve(index, heights):
    cur_height = heights[index]
    
    left_cand = 0
    right_cand = 0
    
    # 왼쪽 높이부터 계산
    if(index > 0):
        for li in range(index - 1, -1, -1):
            if(cur_height <= heights[li]):
                left_cand += 1
            else:
                break
                
    for ri in range(index + 1, n, 1):
        if(cur_height <= heights[ri]):
            right_cand += 1
        else:
            break
                
    left_area = cur_height * left_cand
    right_area = cur_height * right_cand
    total_area = cur_height + left_area + right_area
    
    return total_area

while True:
    n, *heights = list(map(int, input().split()))
    if(n == 0):
        break
    result = []
    
    for i in range(n):
        result.append(solve(i, heights))
    
    print(max(result))




# 방법2 분할정복, 세그먼트 트리
import sys

def max_square(l, r):
    if l == r:
        return h[l]
    else:
        m = (l + r) // 2
        nl = m
        nr = m + 1
        nh = min(h[nl], h[nr])
        tmp = nh * 2

        cnt = 2
        while True:
            if (h[nl] == 0 or nl == l) and (h[nr] == 0 or nr == r): 
                break 
            elif h[nl] == 0 or nl == l:
                if h[nr + 1] < nh:
                    nh = h[nr + 1]
                nr += 1
            elif h[nr] == 0 or nr == r:
                if h[nl - 1] < nh:
                    nh = h[nl - 1]
                nl -= 1
            else:
                if h[nl - 1] > h[nr + 1]:
                    if h[nl - 1] < nh:
                        nh = h[nl - 1]
                    nl -= 1
                else:
                    if h[nr + 1] < nh:
                        nh = h[nr + 1]
                    nr += 1
            cnt += 1
            tmp = max(tmp, nh * cnt)
        return(max(max_square(l, m), max_square(m + 1, r), tmp))  

while True:
    h = list(map(int, sys.stdin.readline().split()))
    if h[0] == 0:
        break
    print(max_square(1, len(h) - 1))




# 방법3 스택
while True:
    n, *heights = list(map(int, input().split()))
    print(heights)
    if(n == 0):
        break
    
    # 첫 시점의 계산을 위해 0을 맨 앞에 추가하고,
    heights.insert(0, 0)
    # 마지막 사각형 계산을 위해 0을 끝에 추가합니다.
    heights += [0]
    checked = [0]
    area = 0
    
    # 현재 높이보다 이전 높이가 높으면, while에 진입합니다.
    # 현재 높이가 더 낮은 경우, 넓이를 이어서 계산할 수 없으므로
    # 이전 시점까지 저장됬던 사각형의 높이를 계산합니다.
    # 끝 사각형도 고려해야 하므로, n+1까지 반복합니다.
    for i in range(1, n + 2):
        # heights[checked[-1]]은 이전 시점의 사각형 높이
        # heights[i]는 현재 시점의 사각형 높이
        # heights[checked[-1]] > heights[i]는 현재 높이보다 이전 높이가 높은지 확인
        while(checked and (heights[checked[-1]] > heights[i])):
            # 비교할 사각형 index
            cur_height = checked.pop()
            # (i - 1 - checked[-1])은 cur_height와 현재 시점 사이에 몇 개의 사각형이 존재하는지를 판단
            area = max(area, (i - 1 - checked[-1]) * heights[cur_height])
        checked.append(i)
    print(area)