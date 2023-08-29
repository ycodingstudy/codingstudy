# 1이 이길 때는 + 1로 한칸, 2가 이길 때는 -1로 한칸
# 0이 되면 비김
# 비기면 1이 이기는 순간이 멈추어저야 한다.
# # 1 -> 1 -> 2 -> 2 -> 2 라고 하면
# (1, 2, 1, 0, -1)이 된다.

# 1이 이기다가 비기면 (전체 경기 시간 - 이기기 시작한 시간) - (전체경기시간 - 비기기 시작한 시간)

n = int(input())

one_time, two_time = 0, 0
flag = 0
for _ in range(n):
    team, time = input().split()
    m, s = map(int, time.split(':'))

    if team == '1':
        if flag == 0:
            one_time += 48 * 60 - (60 * m + s)  # 기존1 + (전체 경기시간 - 이기기 시작한 시간)
        flag += 1  # 1이 이기고 나서
        if flag == 0:  # 무승부가 되면
            if two_time > 0:  #
                two_time -= (48 * 60 - (60 * m + s))  # 기존2 - (전체경기시간 - 지기 시작한 시간)
    else:
        if flag == 0:
            two_time += 48 * 60 - (60 * m + s)
        flag -= 1
        if flag == 0:
            if one_time > 0:
                one_time = one_time - (48 * 60 - (60 * m + s))

print('{:0>2}:{:0>2}'.format(one_time // 60, one_time % 60))
print('{:0>2}:{:0>2}'.format(two_time // 60, two_time % 60))
