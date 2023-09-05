from collections import deque
import sys
n, m, k, x = map(int, sys.stdin.readline().split())

graph = [[] for i in range(n + 1)]
visited = [0 for i in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] += [b]

result = []
def bfs(start_num):
    queue = deque([start_num])
    visited[start_num] = 1
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1 # 여기가 핵심 포인트
                queue.append(i)

                if visited[i] -1 == k:
                    result.append(i)
bfs(x)

result.sort()
if not result:
    print(-1, end = '')

else:
    for i in range(len(result)):
        if i == len(result) - 1:
            print(result[i], end = '')
        else:
            print(result[i])

