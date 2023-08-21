n = int(input())
k = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]  # 보드판 초기화
direction = []  # 방향정보

for _ in range(k):  # 보드 사과 추가
    x, y = map(int, input().split())
    board[x][y] = 1

l = int(input())  # 방향 입력
for _ in range(l):
    x, c = input().split()
    direction.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(dir, c):
    if c == "L":
        dir = (dir - 1) % 4
    else:
        dir = (dir + 1) % 4
    return dir


def simulate():
    x, y = 1, 1  # 시작점
    board[x][y] = 2
    dir, time, index = 0, 0, 0
    q = [(x, y)]
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]

        # 맵 안에 있고, 뱀 몸통이 없다면
        if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] != 2:
            # 사과 없으면 이동 후 꼬리 제거
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                board[px][py] = 0
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))
        else:  # 벽이나 몸통에 부딪혔으면
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < l and time == direction[index][0]:  # 회전해야 하는 경우
            dir = turn(dir, direction[index][1])
            index += 1
    return time


print(simulate())
