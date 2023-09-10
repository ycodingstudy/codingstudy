from collections import deque

n, m, start_num = map(int, input().split())

graph = [[] for i in range(n + 1)]
visited_dfs = [0 for i in range(n + 1)]
visited_bfs = [0 for i in range(n + 1)]
dfs_result = []
bfs_result = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]


for j in graph:
    j.sort()



def dfs(num):
    visited_dfs[num] = 1
    dfs_result.append(num)
    for i in graph[num]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(num):
    queue = deque([num])
    visited_bfs[num] = 1
    while queue:
        x = queue.popleft()
        bfs_result.append(x)
        for i in graph[x]:
            if not visited_bfs[i]:
                visited_bfs[i] = 1
                queue.append(i)

dfs(start_num)
bfs(start_num)

print(*dfs_result)
print(*bfs_result)

