import sys

n, m = map(int, sys.stdin.readline().split())


graph = []
for i in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    graph.append(lst)

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            cnt += 1

print(cnt)