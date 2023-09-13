from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy, visited):
    total = 0
    united_kingdom = []

    q = deque([(sx, sy)])
    visited[sx][sy] = True
    united_kingdom.append((sx, sy))
    total += graph[sx][sy]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    united_kingdom.append((nx, ny))
                    total += graph[nx][ny]

    return united_kingdom, total


cnt = 0
while True:
    flag = False
    
    # 전체를 다 돌아야 하루가 지남
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]: # 흠....
                united, total = bfs(i, j, visited)
                if len(united) > 1:
                    flag = True # graph에 변화가 한 번이라도 생김
                    for x, y in united:
                        graph[x][y] = total // len(united)
    
    if not flag: # 전체를 다 돌아도 그래프에 변화가 안생기면 탈출
        break
    cnt += 1

print(cnt)
