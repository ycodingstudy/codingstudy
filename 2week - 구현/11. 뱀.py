# 사과를 포함한 보드판 완성
n = int(input())  # n x n 보드의 길이
board = [[0] * n for _ in range(n)]
k = int(input())  # k 개의 사과의 위치
for _ in range(k):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1  # 0,0이 1,1이므로 인덱스 조정 필요.

l = int(input())  # 방향 변환 횟수
cmd = []
for _ in range(l):
    x, c = input().split()
    cmd.append((int(x), c))  # x초가 끝난 뒤에 왼쪽(L) 혹은 오른쪽(D)로 회전

# 게임 종료까지 몇 초가 걸리는가?
# 벽, 자기 몸과 부딪히면 게임이 끝남 + 사과를 먹으면 몸 길이가 늘어남
dx = [0, 1, 0, -1]  # 동(0) 남(1) 서(2) 북(3)
dy = [1, 0, -1, 0]


# 현재 동쪽(0)을 보고 있을 때, 'L'을 만나면 북쪽(-1)로 가야하고
# 현재 동쪽(0)을 보고 있을 때, 'R'을 만나면 남쪽(+1)로 가게 됨
def turn(direction, turn_direction):
    if turn_direction == 'L':
        return (direction - 1) % 4
    else:  # 'D' (우회전)
        return (direction + 1) % 4


snake = [[0, 0]]  # snake[0] : 얼굴 위치
time = 0
direction = 0  # 동(0), 남(1), 서(2), 북(3)
cmd_index = 0
while True:
    # 기존 위치 추가(길어질 몸통을 위함)
    next_x = snake[0][0] + dx[direction]
    next_y = snake[0][1] + dy[direction]

    # game over
    if next_x < 0 or next_x >= n or next_y <0 or next_y >=n or [next_x, next_y] in snake:
        break




    if cmd_index < len(cmd) and time == cmd[cmd_index][0]:
        direction = turn(direction, cmd[cmd_index][1])
        cmd_index += 1

    if board[snake[0][0]][snake[0][1]] == 1:
        board[snake[0][0]][snake[0][1]] = 0  # 사과를 먹음
    else:  # board[x][y] == 0
        snake.pop()

    print(snake)

    # game over
    if snake[0][0] >= n or snake[0][1] >= n or snake[0][1] < 0 or snake[0][0] < 0:
        break
    if snake[0] in snake[1:]:
        break

print(time)

# Test case 1
# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

# Test case2
# 10
# 4
# 1 2
# 1 3
# 1 4
# 1 5
# 4
# 8 D
# 10 D
# 11 D
# 13 L

# Test case3
# 10
# 5
# 1 5
# 1 3
# 1 2
# 1 6
# 1 7
# 4
# 8 D
# 10 D
# 11 D
# 13 L
