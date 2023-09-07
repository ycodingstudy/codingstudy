from collections import deque
import sys
input = sys.stdin.readline
# 1 to k 바이러스 종류. 번호가 낮을 수록 먼저 증식
# s 초 후, (x,y)의 바이러스 종류 출력. 존재x면 0출력
dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]
def bfs(viruses, s):
    q = deque()
    time = 0
    for vtype in range(1, len(viruses)):
        for vx, vy in viruses[vtype]:
            q.append((vtype, vx, vy, time))

    while q:
        # [ [(x,y), (x,y)], [(x,y),(x,y)]]
        vtype, vx, vy, time = q.popleft()
        if time == s:
            return
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = vtype
                q.append((vtype, nx, ny, time+1))


n, k = map(int, input().split())
graph = [[0] * n for _ in range(n)]
viruses = [[] for _ in range(k + 1)]  # 인덱스 보정 [[], [(x,y), (x,y)], [(x,y),(x,y)]]
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        graph[i][j] = row[j]
        if row[j] != 0:
            viruses[row[j]].append((i, j))

s, x, y = map(int, input().split())
bfs(viruses, s)
# for g in graph:
#     print(g)
# print("x-1 : {}, y-1 : {}".format(x-1, y-1))
print(graph[x-1][y-1])