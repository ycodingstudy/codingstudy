import sys

n = int(sys.stdin.readline())
graph = []
teacher = []

for i in range(n):
    lst = list(sys.stdin.readline().split())
    graph.append(lst)
    for j, t in enumerate(lst):
        if t == 'T':
            teacher.append([i, j])

flag = False
# 장애물 설치
def backTracking(cnt):
    global flag

    # 3개의 장애물을 설치했다면
    if cnt == 3:
        if bfs():
            flag = True
            return
    else:
        # 모든 빈 공간에 장애물을 3개씩 설치해본다.
        for x in range(n):
            for y in range(n):
                if graph[x][y] == 'X':
                    graph[x][y] = 'O'
                    backTracking(cnt + 1) # backTracking
                    graph[x][y] = 'X'

def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for t in teacher:
        for i in range(4):
            nx, ny = t

            while 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 'O':
                    break

                # 학생이 보이면 실패
                if graph[nx][ny] == 'S':
                    return False

                nx += dx[i]
                ny += dy[i]
    return True

backTracking(0)

if flag:
    print("YES")

else:
    print('NO')




