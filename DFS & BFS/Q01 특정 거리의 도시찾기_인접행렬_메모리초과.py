from collections import deque
import sys
input = sys.stdin.readline
# https://www.acmicpc.net/problem/18352
def bfs(i, K):
    queue = deque([i])
    global graph

    cnt = 0
    visited[i] = True
    result = []
    while queue:
        cnt += 1
        v = queue.popleft()
        for j in range(1, N + 1):
            if graph[v][j] and not visited[j]:
                queue.append(j)
                visited[j] = True
                if cnt == K:
                    result.append(j)
        if cnt == K:
            return result

N, M, K, X = map(int, input().split())
visited = [False] * (N + 1)
graph = [[False] * (N + 1) for _ in range(N + 1)]

# 그래프 체크
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = True
print(graph)
result = bfs(X, K)
if len(result) == 0:
    print(-1)
else:
    for i in sorted(result):
        print(i)
