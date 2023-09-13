import copy
from collections import deque

n = int(input())
graph = [list(map(str, input().split())) for _ in range(n)]
result = "NO"
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
teachers = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == "T":
            teachers.append((i, j))

def searchStudent():
    for x, y in teachers:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while True:
                if 0 > nx or nx >= n or 0 > ny or ny >= n or graph[nx][ny] == "B": #범위를 벗어나거나 장애물을 만나면
                    break
                if graph[nx][ny] == "S": #학생을 만나면
                    return
                nx += dx[i]
                ny += dy[i]
    global result
    result = "YES"



def dfs(cnt):
    if cnt == 3:
        searchStudent()
        return

    for i in range(n):
        for j in range(n):
            if graph[i][j] == "X":
                graph[i][j] = "B"
                dfs(cnt+1)
                graph[i][j] = "X"

dfs(0)
print(result)