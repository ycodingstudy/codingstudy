from collections import deque
import sys, copy
input = sys.stdin.readline

n, m = map(int, input().split()) # n : 세로, m : 가로
space = [list(map(int, input().split())) for _ in range(n)]
tmp_space = copy.deepcopy(space)

# 남, 동, 북, 서
# 남쪽을 시작으로 반시계방향으로 돌아가는 순서로 되어 있음
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 사무실의 범위를 벗어나는지 체크해주는 함수
def check(row, col):
    return row < 0 or row >= n or col < 0 or col >= m

def init():
    obj = deque() # cctv 위치 저장 큐
    ans = 0
    for i in range(n):
        for j in range(m):
            # 벽X, 빈칸 X
            if space[i][j] != 6 and space[i][j] != 0:
                # cctv 번호, 좌표 저장(y, x)
                obj.append((space[i][j], i, j))
            # cctv가 없는 '빈칸의 개수'를 카운트
            if space[i][j] == 0:
                ans += 1
    return obj, ans

cctv, ans = init()

# 감시
def move(y, x, direction):
    direction %= 4
    while True:
        y += dy[direction]
        x += dx[direction]
        # 범위를 벗어났거나 벽을 만났다면 return
        if check(y, x) or tmp_space[y][x] == 6:
            return
        # 빈칸이아니면
        if tmp_space[y][x] != 0:
            continue
        # 빈칸이면
        tmp_space[y][x] = '#'

# 각 cctv에 대해 모든 방향을 고려해 모든 경우의 수를 구함
for i in range(4**len(cctv)):
    case = i
    tmp_space = copy.deepcopy(space)

    for j in range(len(cctv)):
        d = case % 4
        case //= 4

        num, y, x = cctv[j]

        # cctv번호 별로 가르키는 방향으로 이동함
        # 이 부분을 간결하게 작성하려면 어떻게 해야할까 (고민)
        if num == 1:
            move(y, x, d)
        elif num == 2:
            move(y, x, d);
            move(y, x, d + 2)
        elif num == 3:
            move(y, x, d);
            move(y, x, d + 1)
        elif num == 4:
            move(y, x, d);
            move(y, x, d + 1);
            move(y, x, d + 2)
        else:
            move(y, x, d);
            move(y, x, d + 1);
            move(y, x, d + 2);
            move(y, x, d + 3)

        # 하나의 case에서 수행을 다 마치면 사각 지대의 개수를 구함
    zero_cnt = 0
    for i in tmp_space:
        zero_cnt += i.count(0)
    answer = min(zero_cnt, answer)
print(answer)