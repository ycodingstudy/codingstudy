n, m = map(int, input().split())
x, y, d = map(int, input().split())  # 방향 : 0북, 1동, 2남, 3서

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = []
for row in range(n):
    board.append(list(map(int, input().split())))

cnt = 0
while True:
    if board[x][y] == 0:
        cnt += 1
        board[x][y] = -1  # 청소 완료

    can_move = False
    for i in range(4):  # 반시계 방향으로 확인(d와 관련지어야함)
        d = (d - 1 + 4) % 4
        next_x = x + dx[d]
        next_y = y + dy[d]

        if 0 <= next_x < n and 0 < next_y < m and board[next_x][next_y] == 0:
            x, y = next_x, next_y  # 전진
            can_move = True
            break

    if not can_move:  # 4칸 중 청소되지 않은 빈칸이 없는 경우
        back = (d + 2) % 4
        back_x = x + dx[back]
        back_y = y + dy[back]
        if board[back_x][back_y] == 1:
            break
        else:
            x, y = back_x, back_y

# print("x : ", x, "y : ", y)
# for row in board:
#     print(row)
print(cnt)
