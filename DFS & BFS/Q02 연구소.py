from collections import deque
import sys
import copy
#https://www.acmicpc.net/problem/14502
#1시간 35분 소요
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
# 0 = 빈칸, 1 = 벽, 2 = 바이러스, 벽의 수는 항상 3개
#안전구역 카운트하기
def countSafezone(lab):
    safeCnt = 0
    for i in range(n):
        safeCnt += lab[i].count(0)
    return safeCnt

#bfs로 바이러스 퍼뜨리기
def bfs():
    q = deque()
    lab = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                q.append((i,j))
    while q:
        x, y = q.popleft()

        for i in range(4):
           nx = x + dx[i]
           ny = y + dy[i]
           if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == 0:
               q.append((nx,ny))
               lab[nx][ny] = 2
    global result
    result = max(countSafezone(lab), result)


#벽 세우기
def createWall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                createWall(cnt+1)
                graph[i][j] = 0

result = 0
createWall(0)
print(result)