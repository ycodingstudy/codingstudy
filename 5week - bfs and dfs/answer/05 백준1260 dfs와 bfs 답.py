from collections import deque

n, m, v = map(int, input().split())

# 인접 행렬
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# 방문 리스트 행렬
visited1 = [False] * (n + 1)
visited2 = visited1.copy()


def dfs(v):
    visited1[v] = True
    print(v, end='')
    for i in range(1, n + 1):
        if graph[v][i] == 1 and visited1[i] == False:
            dfs(i)


def bfs(v):
    q = deque(v)
    visited2[v] = True
    while q:
        node = q.popleft()
        print(node, end=' ')
        for i in range(1, n + 1):
            if not visited2[node] and graph[node][i] == 1:
                q.append(i)
                visited2[i] = True

dfs(v)
print()
bfs(v)