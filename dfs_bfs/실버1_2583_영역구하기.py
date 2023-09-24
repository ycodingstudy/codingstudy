import sys
from collections import deque

# m,n,k 입력
m, n, k = map(int, sys.stdin.readline().split())
graph = [[0 for i in range(n)] for j in range(m)]

# 영역 입력(색칠 해주기)
for _ in range(k):
    x, y, ax, ay = map(int, sys.stdin.readline().split()) # 0 2 4 4
    for i in range(y, ay): # 2 4
        for j in range(x, ax): # 0 4
            graph[i][j] = 1

def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque([[x, y]])
    graph[x][y] = 1
    cnt = 1
    while queue:
        bx, by = queue.popleft()

        for i in range(4):
            tx = bx + dx[i]
            ty = by + dy[i]

            if (0 <= tx < m and 0 <= ty < n) and not graph[tx][ty] : # 그래프를 넘지 않으면서 색칠 안된곳 색칠 하기
                graph[tx][ty] = 1
                queue.append([tx, ty])
                cnt += 1
    return cnt

result = []
for i in range(m):
    for j in range(n):
        if not graph[i][j]:
            area = bfs(i, j) # return 받은 cnt area에 담기
            result.append(area) # result에 cnt 담기

print(len(result))
print(*sorted(result))

