# 아이디어는 조합으로 3개를 벽세우고 (Collection 활용)
# BFS를 통해서 안전구역을 세자
import sys
from itertools import combinations
from collections import deque
import copy

n, m = map(int, sys.stdin.readline().split())

graph = []
blank_coordinate = []
virus_coordinate = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if lst[j] == 0:  # 빈 곳 좌표 저장
            blank_coordinate.append([i, j])
        elif lst[j] == 2:  # 바이러스 좌표 저장
            virus_coordinate.append([i, j])
    graph.append(lst)


def bfs(graph):
    queue = deque(virus_coordinate)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]

            if ax < 0 or ax >= n or ay < 0 or ay >= m:
                continue

            elif graph[ax][ay] == 0:
                graph[ax][ay] = 2
                queue.append([ax, ay])
    cnt = 0
    for i in range(n):
        cnt += graph[i].count(0)
    return cnt


combinations_coordinate = list(combinations(blank_coordinate, 3))

result = 0
for combinations_part in combinations_coordinate:  # 0인곳 벽치기
    copy_graph = copy.deepcopy(graph)
    for i in range(3):
        # 0인 곳 1로 벽 세우기
        copy_graph[combinations_part[i][0]][combinations_part[i][1]] = 1
    result = max(result, bfs(copy_graph))


print(result)
