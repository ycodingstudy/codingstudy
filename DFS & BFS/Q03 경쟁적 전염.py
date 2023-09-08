import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
visited = [[0] * (n) for i in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]

s, y, x = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def checkVirus(v, y, x, cnt):  # 특정 종류의 바이러스만
    visited[x][y] = cnt+1
    for i in range(4): #상하좌우
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] == 0: #범위를 안넘고 빈 땅이라면
            graph[nx][ny] = v
            visited[nx][ny] = cnt+2

for cnt in range(s):
    flag = True
    for v in range(1, k + 1):
        for i in range(n):
            for j in range(n):
                if graph[i][j] == v and visited[i][j] == cnt:
                    checkVirus(v, j, i, cnt)
                if graph[i][j] == 0: #전염이 안된 부분이 있다면
                    flag = False
    if flag: #모두 전염이 됐다면
        break

print(graph[y-1][x-1])