# https://www.acmicpc.net/problem/2583
#
# 5 7 3 (m, n, k) : m(row, y), n(col, x)
# k개의 줄에 직사각형의 좌표가 주어짐
# 0 2 4 4 # 좌측 아래 꼭지점의 x, y값 && 우측 위 꼭짓 짓점의 x, y
# 1 1 2 5
# 4 0 6 2
#
from collections import deque

m, n, k = map(int, input().split())  # 5 7 3
graph = [[0] * n for _ in range(m)] # visited 역할을 함
for _ in range(k):
    # 0 2 4 4 / 1 1 2 5 / 4 0 6 2
    x1, y1, x2, y2 = map(int, input().split())
    y1 = m - y1 - 1  # 5-2 = 3 (좌측 아래) / 5 - 1 = 4 / 5 - 0 = 5
    y2 = m - y2 - 1  # 5-4 = 1 (우측 위) / 5 - 5 = 0   / 5 - 2 = 3
    for y in range(y1, y2, -1):  # 3 to 1 (3 2) / 4 to 0 (4 3 2 1) / 5 to 3(5,4)
        for x in range(x1, x2):  # 0 to 4 (0,1,2,3)/ 1 to 2(0, 1) / 4 to 6(4, 5)
            graph[y][x] = 1

# for row in graph:
#     print(row)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(sx, sy, graph):
    q = deque([(sx, sy)])
    graph[sy][sx] = 2  # 1로 해도 됨
    size = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == 0:
                q.append((nx, ny))
                graph[ny][nx] = 2
                size += 1
    return size


res = []
for i in range(0, m):
    for j in range(0, n):
        if graph[i][j] == 0:
            size = bfs(j, i, graph)
            res.append(size)

res.sort()
print(len(res))
print(*res)

# for row in graph:
#      print(row)