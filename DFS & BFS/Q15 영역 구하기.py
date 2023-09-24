import sys; sys.setrecursionlimit(10**6)
m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]
box = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 박스좌표 입력받기
for _ in range(k):
    b = list(map(int, input().split()))
    for i in range(b[0], b[2]):  # 박스 좌표를 통해 graph에 박스 표시하기
        for j in range(b[1], b[3]):
            graph[j][i] = 1

def dfs(x, y):
    global boxSize
    if 0 > x or x >= m or 0 > y or y >= n or graph[x][y] == 1:
        return
    boxSize += 1
    graph[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx,ny)

cnt = 0
result = []
boxSize = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            cnt += 1
            dfs(i, j)
            result.append(boxSize)
            boxSize = 0

result.sort()
print(cnt)
print(*result)