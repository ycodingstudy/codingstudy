# https://www.acmicpc.net/problem/1012
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(sx, sy, visited):
    q = deque([(sx, sy)])
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                # 배추가 없는 부분을 지나가지 않도록 이미 있는 부분인지 확인
                if graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))

t = int(input())  # test case 수
for _ in range(t):
    m, n, k = map(int, input().split())  # m : 가로, n : 세로, k : 배추 위치 수

    graph = [[0] * m for _ in range(n)]
    vegetables = []
    for _ in range(k):
        # (x, y) 에서 x가 가로(col), y가 세로(row)
        tmp = tuple(map(int, input().split()))  # (0, 0)
        vegetables.append(tmp)
        graph[tmp[1]][tmp[0]] = 1

    visited = [[False] * m for _ in range(n)]

    cnt = 0
    for sy, sx in vegetables:
        # bfs의 수행 횟수를 카운트함
        if not visited[sx][sy]:
            bfs(sx, sy, visited)
            cnt += 1

    print(cnt)


