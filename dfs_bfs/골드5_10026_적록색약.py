import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

normal_graph = []
color_graph = []
visited_normal = [[0 for i in range(n)] for j in range(n)]
visited_color = [[0 for i in range(n)] for j in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


for _ in range(n):
    normal_str = sys.stdin.readline().rstrip()
    normal_graph.append(list(normal_str))
    color_str = normal_str.replace('G', 'R') # 처음부터 분리해서 그래프를 하나 더 만듬
    color_graph.append(list(color_str))

def bfs(graph, visited, target_x, target_y):
    queue = deque([[target_x, target_y]])
    visited[target_x][target_y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]

            if ax < 0 or ax >= n or ay < 0 or ay >= n:
                continue

            elif (graph[ax][ay] == graph[x][y]) and not visited[ax][ay]:
                queue.append([ax, ay])
                visited[ax][ay] = 1


normal_cnt = 0
color_cnt = 0
for i in range(n):
    for j in range(n):
        if not visited_normal[i][j]:
            bfs(normal_graph, visited_normal, i, j)
            normal_cnt += 1

        if not visited_color[i][j]:
            bfs(color_graph, visited_color, i, j)
            color_cnt += 1

print(normal_cnt, color_cnt, end = '')