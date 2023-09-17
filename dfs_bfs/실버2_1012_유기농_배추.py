import sys
from collections import deque

def bfs(graph, a, b):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([[a, b]])
    graph[a][b] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]

            if ax < 0 or ax >= m or ay < 0 or ay >= n:
                continue

            elif graph[ax][ay] == 1:
                graph[ax][ay] = 0
                queue.append([ax, ay])

num = int(input())

for _ in range(num):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0 for i in range(n)] for j in range(m)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1
    cnt = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                cnt += 1
    print(cnt)

