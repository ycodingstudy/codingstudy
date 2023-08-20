n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]  # map
info = []  # 방향 회전 정보

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

dx = [0, 1, 0, -1]  # 동, 남, 서, 북
dy = [1, 0, -1, 0]


def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


def simulate():
    x, y = 1, 1  # head
    data[x][y] = 2  # 뱀이 존재하는 위치는 2로 표시
    direction = 0  # 보고 있는 방향 (동)
    time = 0
    index = 0  # 다음에 회전할 정보
    q = [(x, y)]  # 뱀이 차지하고 있는 정보 위치 (꼬리 to 머리)

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)  # 꼬리부분(가장 앞쪽)을 제거
                data[px][py] = 0  # 뱀이 없다고 표시해줌
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        else:  # 벽 or 몸통에 부딪힘
            time += 1
            break
        x, y = nx, ny  # 다음 위치로 머리를 이동 시킴
        time += 1
        if index < l and time == info[index][0]:  # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time


print(simulate())
