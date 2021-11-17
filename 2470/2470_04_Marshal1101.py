# 2470 03 두 용액 (완료)

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
data.sort()
min_idx = []
left = 0
right = n-1
arr = 0

min_idx = [left, right]
min_gap = abs(data[left] + data[right])

while(left < right):
    if abs(data[left] + data[right]) < min_gap:
        min_gap = abs(data[left] + data[right])
        min_idx=[left, right]
        
    left_r = data[left+1] + data[right]
    right_l = data[left] + data[right-1]
    
    if abs(left_r) < abs(right_l):
        left += 1
    else:
        right -= 1
        
print(str(data[min_idx[0]])+" "+str(data[min_idx[1]]))



# ## 2470 4 두 용액 (작성자: 김지훈)

# import sys  
# sys.setrecursionlimit(10**8)
# input = sys.stdin.readline

# n = int(input())
# L = list(map(int, input().split()))
# L.sort()

# al = 0
# ar = n- 1
# amin = abs(L[al] + L[ar])

# def Bsearch(l, pl, pr) :
#     global amin, al, ar
#     if pl >= pr :
#         return [amin, al, ar]
#     sum = l[pl] + l[pr]
#     if abs(sum) < amin :
#         amin = abs(sum)
#         al = pl
#         ar = pr
#     if sum == 0 :
#         return [amin, al, ar]
#     if sum > 0 :
#         return Bsearch(l, pl, pr - 1)
#     else :
#         return Bsearch(l, pl + 1, pr)

# ans = Bsearch(L, al, ar)
# print(L[ans[1]], L[ans[2]])
            