# 적록색약 : https://www.acmicpc.net/problem/10026
# N*N grid에 RGB
# 같은 색상이 상하좌우 인접 -> 같은 구역 (or 색상 구분 못해도 같은 구역)
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())

graph_normal = []
graph_problem = []
for _ in range(n):
    row = list(input())
    graph_normal.append(row)
    new_row = []
    for i in range(n):
        if row[i] == 'R':
            new_row.append('G')
        else:
            new_row.append(row[i])
    graph_problem.append(new_row)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited_normal = [[False] * n for _ in range(n)]
def dfs_normal(x, y, color):
    visited_normal[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited_normal[nx][ny]:
            if graph_normal[nx][ny] == color:
                dfs_normal(nx, ny, color)

def cnt_regions_normal():
    regions = 0
    for i in range(n):
        for j in range(n):
            if not visited_normal[i][j]:  # 앞에서 방문한 것은 굳이 방문할 필요 없음.
                dfs_normal(i, j, graph_normal[i][j])
                regions += 1
    return regions


visited_problem = [[False] * n for _ in range(n)]
def bfs_problem(x, y, color):
    q = deque([(x, y)])
    visited_problem[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited_problem[nx][ny]:
                if graph_problem[nx][ny] == color:
                    visited_problem[nx][ny] = True
                    q.append((nx, ny))

def cnt_regions_problem():
    regions = 0
    for i in range(n):
        for j in range(n):
            if not visited_problem[i][j]:
                bfs_problem(i, j, graph_problem[i][j])
                regions += 1
    return regions

normal_cnt = cnt_regions_normal()
problem_cnt = cnt_regions_problem()
print(normal_cnt, problem_cnt)
