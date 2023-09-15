import sys; input = sys.stdin.readline
from collections import deque

n, l, r = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
day = 0
def bfs(sx ,sy):
    # 조건. 만약 공유하는 나라의 인구 차이가 안나면 return
    global flag, visited
    openLand = []
    q = deque()
    q.append((sx, sy))
    openLand.append((sx, sy, land[sx][sy]))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 1.만약 현재 인접한 나라에서 l보다 작고 r보다 큰 나라가 있는지 확인
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and (l <= abs(land[x][y] - land[nx][ny]) <= r):
                # 2.해당 나라를 큐에 추가하고 리스트에 좌표와 해당 나라의 인구수 추가, 1부터 반복
                openLand.append((nx, ny, land[nx][ny]))
                q.append((nx,ny))
                visited[nx][ny] = True
                flag = True


    #3.국경이 열린 나라들의 평균을 구하고, 해당 나라들에 입력
    if flag: #국경이 열렸으면
        landCnt = len(openLand)
        total = 0
        for i in range(landCnt):
            _, _, val = openLand[i]
            total += val
        avg = int(total / landCnt)
        for i in range(landCnt):
            x, y, val = openLand[i]
            land[x][y] = avg

while True:
    flag = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                bfs(i, j)
    if flag:
        day += 1
    else:
        print(day)
        break
