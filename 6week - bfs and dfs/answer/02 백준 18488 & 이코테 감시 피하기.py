from itertools import combinations

n = int(input())
board = []
teachers = []
spaces = [] # 빈 공간의 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        elif board[i][j] == 'X':
            spaces.append((i, j))

# 특정 방향으로 감시 진행(학생 발견 : T, 학생 미발견 F)
def watch(x, y, direction):
    # Left
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
    # Right
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    # Up
    if direction == 2:
        while x>= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
    # Down
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    return False

# 장애물 설치 이후에, 한 명이라도 학생이 감지되는 지 검사
def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지 여부
for data in combinations(spaces, 3):
    for x, y in data:
        board[x][y] = 'O'

    if not process(): # 학생이 한 명도 감지되지 않느 경우
        find = True # 원하는 바를 발견
        break

    # 설치된 장애물 다시 없애기
    for x, y in data:
        board[x][y] = 'X'

if find:
    print("YES")
else:
    print("NO")