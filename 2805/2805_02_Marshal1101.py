#2805  02 나무 자르기 (완료)
import sys

n, m = map(int,sys.stdin.readline().split())
tree_list = list(map(int,sys.stdin.readline().split()))
start = 0
end = max(tree_list)
max_h = 0
tree_list.sort(reverse=True)

def cutter(start, end, m):
    global max_h

    if start > end:
        return max_h

    center = (start + end) // 2
    expec = 0
    for tree in tree_list:
        if tree > center:
            expec += (tree - center)
            if expec > m:
                max_h = center
                cutter(center+1, end, m)
                break
    else:
        if expec == m:
            max_h = center
        elif expec < m:
            cutter(start, center-1, m)
    return max_h

cutter(start, end, m)
print(max_h)