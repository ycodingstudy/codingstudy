import sys
from collections import deque

m, n, k = map(int, sys.stdin.readline().split())
graph = [[0 for i in range(n)] for j in range(m)]

for _ in range(k):
    x, y, ax, ay = map(int, sys.stdin.readline().split())
    for i in range(y, ay):
        for j in range(x, ax):
            graph[i][j] = 1

def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque([[x, y]])
    graph[x][y] = 1
    c = 1
    while queue:
        bx, by = queue.popleft()

        for i in range(4):
            tx = bx + dx[i]
            ty = by + dy[i]

            if (0 <= tx < m and 0 <= ty < n) and not graph[tx][ty] :
                graph[tx][ty] = 1
                queue.append([tx, ty])
                c += 1
    return c

result = []
for i in range(m):
    for j in range(n):
        if not graph[i][j]:
            area = bfs(i, j)
            result.append(area)

print(len(result))
print(*sorted(result))

