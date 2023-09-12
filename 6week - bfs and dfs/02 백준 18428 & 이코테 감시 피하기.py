from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = []
teachers = []
for i in range(n):
    row = list(map(str, input().split()))
    graph.append(row)
    for j in range(n):
        if row[j] == 'T':  # board[i][j] 와 동일
            teachers.append([i, j])


# make wall을 하며 전체를 start 시킴
find_student = False
def make_wall_dfs(wall_cnt):
    global find_student
    if wall_cnt == 3:
        if not bfs(teachers): # bfs : 학생 발견시 True, 미발견시 False
            find_student = True
        return
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                make_wall_dfs(wall_cnt + 1)
                graph[i][j] = 'X'


def look_straight(x, y, i):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0  # 학생 수
    # i : 0, 1, 2, 3 / 상 하 좌 우
    while True:
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or n <= nx or ny < 0 or n <= ny:
            break
        if graph[nx][ny] == 'O':
            break
        elif graph[nx][ny] == 'S':
            cnt += 1
        x, y = nx, ny
    return cnt


def bfs(teacher_lst):
    q = deque(teacher_lst) # [[x1, y1], [x2, y2], [x3, y3], ... ]
    while q:
        x, y = q.popleft()
        for i in range(4):
            std_num = look_straight(x, y, i)
            if std_num != 0:
                return True # 학생 발견
    return False # 학생 미발견

make_wall_dfs(0)
if find_student:
    print("YES")
else:
    print("NO")