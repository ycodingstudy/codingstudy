from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

t = int(input())

def bfs(graph, sx, sy):
    q = deque([(sx, sy)])
    graph[sx][sy] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))

for i in range(4):
    cnt = 0
    n, m, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for sx in range(n):
        for sy in range(m):
            if graph[sx][sy] == 1:
                bfs(graph, sx, sy)
                cnt += 1
    print(cnt)