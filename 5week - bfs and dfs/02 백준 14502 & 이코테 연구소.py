# 0 : 빈 칸, 1 : 벽, 2 : 바이러스
# 벽 세우기(최대 3개) -> 바이러스 번식 -> 안전영역(0카운트)
import sys
from itertools import combinations

input = sys.stdin.readline

dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
dy = [0, 0, -1, 1]


def dfs(g, x, y):  # 바이러스가 퍼짐 (x와 y는 바이러스 위치)
    g[x][y] = 2  # 1) 방문체크

    for i in range(4):  # 2) 4방향 확인
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 0:
            dfs(g, nx, ny)


#  =====  main =====
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

walls, virus = [], []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:  # 벽 위치 가능 부분
            walls.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))  # 바이러스 위치 파악

cnt_lst = []
for wall in combinations(walls, 3):  # ((0, 1), (0, 2), (0, 3)), ((), (), ())
    # 1. graph초기화
    g = [row[:] for row in graph]

    # 2. 벽을 막음
    for x, y in wall:
        g[x][y] = 1
    # 3. 바이 러스 퍼짐
    for x, y in virus:
        dfs(g, x, y)

    # 4. 안전한 곳 카운트
    cnt = 0
    for row in g:
        cnt += row.count(0)
    cnt_lst.append(cnt)

print(max(cnt_lst))
