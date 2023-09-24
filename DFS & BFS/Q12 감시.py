import sys
import copy

n, m = map(int, input().split())
cctv_list = []
graph = []
min_val = int(1e9)
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)
    for j in range(m):
        if 0 < temp[j] < 6:
            cctv_list.append((temp[j], i, j))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
mod = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 2], [1, 2], [1, 3], [0, 3]],
    [[0, 1, 2], [1, 2, 3], [0, 2, 3], [0, 1, 3]],
    [[0, 1, 2, 3]]
]

def check(copy_graph):
    cnt = 0
    for g in copy_graph:
        cnt += g.count(0)
    return cnt

def watch(copy_graph, mode, cctv):
    v, x, y = cctv
    for i in mod[v][mode]:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or copy_graph[nx][ny] == 6:
                break
            if 0 < copy_graph[nx][ny] < 6:
                continue
            copy_graph[nx][ny] = -1

def dfs(depth, copy_graph):
    global min_val
    if depth == len(cctv_list):
        min_val = min(check(copy_graph), min_val)
        return
    v, x, y = cctv_list[depth]
    for mode in range(len(mod[v])):
        temp_graph = copy.deepcopy(copy_graph)
        watch(temp_graph, mode, cctv_list[depth])
        dfs(depth+1, temp_graph)

dfs(0, graph)
print(min_val)
