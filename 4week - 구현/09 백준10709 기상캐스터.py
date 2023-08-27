h, w = map(int, input().split())

board = [[-1] * w for _ in range(h)]
for i in range(h):
    row = input()
    for j in range(w):
        if row[j] == 'c':
            board[i][j] = 0  # 처음에 구름이 떠 있던 경우
        elif j != 0:  # and row[j] == '.'
            time = 0
            for k in range(j - 1, -1, -1): # 거꾸로 가면서 가장 가까운 구름과의 거리(시간) 확인
                time += 1
                if row[k] == 'c':
                    board[i][j] = time
                    break

# 출력
for row in board:
    print(" ".join(str(item) for item in row))
