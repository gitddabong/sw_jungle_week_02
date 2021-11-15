import sys

# 시작점 x,y 와 사각형 크기를 받아서 그 사각형이 모두 같은 색상인지 검사
def is_color_same(size, x, y):
    # 비교용으로 쓸 사각형 시작점 색깔 받아오기
    start_val = paper[x][y]
    
    for i in range(x, size + x):
        for j in range(y, size + y):
            # 시작점이랑 색이 다르면 바로 False 반환
            if paper[i][j] != start_val:
                return False
    return True

# 시작점과 사이즈를 넘겨받아 작업 수행
def partition(size, x = 0, y = 0):
    global white, blue
    # 선택된 사각형의 색이 모두 같으면 그 색에 맞게 카운트 +1
    if is_color_same(size, x, y) == True:
        if paper[x][y] == 0:
            white += 1
            return
        else:
            blue += 1
            return

    half = size // 2

    partition(half, x, y)           # 1번째 사각형
    partition(half, x, y + half)    # 2번째 사각형
    partition(half, x + half, y)    # 3번째 사각형
    partition(half, x + half, y + half) # 4번째 사각형

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())

    paper = []
    for i in range(n):
        paper.append(list(map(int, input().split())))

    # 흰색, 파란색 사각형 개수
    white = 0
    blue = 0

    partition(n)
    
    print(white)
    print(blue)