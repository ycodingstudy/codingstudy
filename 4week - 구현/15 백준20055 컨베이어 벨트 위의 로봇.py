# 로봇은 올리는 위치에만 올릴 수 있음. 내리는 위치 도달시 즉시 내림
# 컨베이너 벨트 위에서 로봇은 스스로 이동 가능 + 로봇이 있는 칸의 내구도는 -1됨

# 로봇을 옮기는 과정
def move(lst):
    res = lst[-1:] + lst[:-1]
    return res


# 로봇은 1부터 n까지만 이동함
n, k = map(int, input().split())
conveys = list(map(int, input().split()))
robots = [0] * n

level = 0
while True:
    level += 1

    conveys = move(conveys)
    robots = move(robots)
    robots[-1] = 0

    for i in range(n - 2, -1, -1):
        if robots[i] == 1 and robots[i + 1] == 0 and conveys[i + 1] >= 1:
            robots[i] = 0
            robots[i + 1] = 1  # 로봇 이동
            conveys[i + 1] -= 1  # 내구도 감소
    robots[-1] = 0 # 로봇 내림

    if conveys[0] != 0 and robots[0] != 1:  # 로봇 올리기
        robots[0] = 1  # 로봇이 올라감
        conveys[0] -= 1  # 내구도 감소

    if conveys.count(0) >= k:
        break

print(level)
