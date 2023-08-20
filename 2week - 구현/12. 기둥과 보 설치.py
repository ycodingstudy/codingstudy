# 2차원 가상 벽면에 기둥과 보를 이용한 구조물 설치
# 기둥과 보는 길이가 1인 선분으로 표현 됨
# - 기둥은 바닥 위에 있거나 보의 한쪽 끝부분 위에 있거나, 다른 기둥 위
# - 보는 한쪽 끝 부분이 기둥 위 or 양쪽 끝 부분이 다른 보와 동시에 연결

def check(board, x, y, obj):
    if obj == 0:  # 기둥
        if y == 0: return True # 바닥 위
        if board[x-1][y] == 1: return True # 보의 한쪽 끝 위
        if board[x][y] == 1: return True # 보의 한쪽 끝 위
        if board[x][y-1] == 0: return True # 또 다른 기둥
    else:  # 보
        if board[x][y-1] == 0 or board[x+1][y-1] == 0: return True # 한쪽 끝 부분이 기둥 위
        if board[x-1][y] == 1 and board[x+1][y] == 1: return True # 양쪽 끝 부분이 다른 보와 동시 연결

    return False




def solution(n, build_frame):
    board = [[-1] * (n + 1) for _ in range(n + 1)]

    # row : [xy, 기둥(0)or 보(1), 삭제(0) or 설치(1)]
    for row in build_frame:
        x, y = row[0], row[1]
        if row[3] == 0:  # 삭제
            tmp = board[x][y] # backup
            board[x][y] = -1 # 우선 삭제
            if not check(board, x, y, row[2]):
                board[x][y] = tmp
        else:  # 설치하는 경우
            if check(board, row[0], row[1], row[2]):
                board[x][y] = row[2]  # 기둥은 0, 보는 1을 설치

    # 설치한 것을 확인해서 출력 [x, y, 무엇 인지]
    res = []
    for i in range(n + 1):
        for j in range(n + 1):
            if board[i][j] != -1:
                res.append([i, j, board[i][j]])
    return res


n = 5
build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1],
               [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1],
               [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0],
               [2, 2, 0, 1]]
res = solution(n, build_frame)
print(res)
