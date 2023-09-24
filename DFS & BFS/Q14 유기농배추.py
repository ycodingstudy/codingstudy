import sys
sys.setrecursionlimit(10**6)
t = int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
result = []

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m or graph[x][y] == 0:
        return
    graph[x][y] = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        dfs(nx,ny)
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k): #배추 위치 찍기
        y, x = map(int, input().split())
        graph[x][y] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    result.append(cnt)

for p in result:
    print(p)