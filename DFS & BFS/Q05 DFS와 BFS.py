#https://www.acmicpc.net/problem/1260
#32분 소요
import sys; input = sys.stdin.readline
from collections import deque
n, m, v = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
def dfs(v):
    visited[v] = True
    print(v, end = " ")
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(i)

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        node = q.popleft()
        print(node, end=" ")
        for i in sorted(graph[node]):
            if not visited[i]:
                visited[i] = True
                q.append(i)

dfs(v)
visited = [False] * (n+1)
print("")
bfs(v)
