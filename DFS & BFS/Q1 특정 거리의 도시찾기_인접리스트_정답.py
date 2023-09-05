# https://www.acmicpc.net/problem/18352
from collections import deque, defaultdict
import sys
f = sys.stdin.readline
def bfs(X, K):
    result = []
    queue = deque([X])
    distance = [0] * (N + 1)
    visited[X] = True
    global graph

    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
                distance[node] = distance[v] + 1
                if distance[node] == K:
                    result.append(node)
    return result

N, M, K, X = map(int, f().split())
visited = [False] * (N + 1)
graph = [[] for _ in range(N+1)]
# 그래프 체크
for _ in range(M):
    x, y = map(int, f().split())
    graph[x].append(y)
result = bfs(X, K)
if len(result) == 0:
    print(-1)
else:
    for i in sorted(result):
        print(i)

