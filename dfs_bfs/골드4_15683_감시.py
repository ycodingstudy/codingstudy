import copy
n, m = map(int, input().split())
cctv = [] # CCTV종류, x좌표, y좌표
board = [] # 사무실 정보

#CCTV 방향정보
mode = [
    [],
    [[0], [1], [2], [3]], # 1번 CCTV
    [[0, 2], [1, 3]], # 2번
    [[0, 1], [1, 2], [2, 3], [0, 3]], # 3번
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]], # 4번
    [[0, 1, 2, 3]]# 5번
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    data = list(map(int, input().split()))
    board.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j])

def fill(board, mode, x, y):
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            # 범위를 넘어가면 중단
            if nx < 0 or ny < 0 or nx >=n or ny >=m:
                break
            # 벽이면 중단
            if board[nx][ny] == 6:
                break
            # 감시가능
            elif board[nx][ny] == 0:
                board[nx][ny] = -1

def dfs(depth, board):
    global min_value
    if depth == len(cctv): # 탐색완료
        count = 0
        for i in range(n): # 사각지대 찿기
            count += board[i].count(0)
        # 최소값 업데이트
        min_value = min(min_value, count)
        return

    temp = copy.deepcopy(board) # 보드 복제
    cctv_num, x, y = cctv[depth] # 탐색할 CCTV
    for i in mode[cctv_num]: # CCTV의 방향에 따라서
        fill(temp, i, x, y) # 감시 시작
        dfs(depth + 1, temp) # 재귀 호출
        temp = copy.deepcopy(board) # 보드 초기화

min_value = int(1e9)
dfs(0, board)
print(min_value)