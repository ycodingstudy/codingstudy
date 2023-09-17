import sys; input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[False] * (n) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

#일반, 색약 구역 카운트
cnt, blindCnt = 0, 0
def bfs(sx,sy,color):
    q = deque([(sx,sy)])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] in color: #입력받은 색과 같다면(색약의 경우 [RG], [B] 일반이라면 [R], [G], [B]
                    visited[nx][ny]= True
                    q.append((nx,ny))

for i in range(n): #일반 카운트
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, graph[i][j])
            cnt+=1

visited = [[False] * (n) for _ in range(n)]
for i in range(n): #색약 카운트
    for j in range(n):
        if not visited[i][j]:
            if graph[i][j] != "B":
                bfs(i, j, ["R","G"])
            else:
                bfs(i, j, graph[i][j])
            blindCnt += 1
print(cnt, end=" ")
print(blindCnt, end=" ")
