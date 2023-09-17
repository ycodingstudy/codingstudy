from collections import deque
N, K = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
virus_info = []

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N): # 바이러스의 위치와 종류를 저장
        if graph[i][j] != 0:
            virus_info.append(((graph[i][j], i, j)))
S, X, Y = map(int, input().split())

def bfs(s, X, Y):
    q = deque(virus_info)
    count = 0
    while q:
        if count == s:
            break
        for _ in range(len(q)):
            prev, x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y]
                        q.append((graph[nx][ny], nx, ny))
        count += 1
    return graph[X - 1][Y - 1]


virus_info.sort()
print(bfs(S, X, Y))
