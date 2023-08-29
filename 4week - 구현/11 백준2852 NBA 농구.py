# [문제 이해를 못함;;;;;;;;]
# 골이 들어간 시간 , 골 넣은 팀 (1팀 or 2팀)
# 48분 진행

n = int(input())
one_win_time, two_win_time = 0, 0  # 초로 관리
prev_team, cur_team = '', ''
prev_m, prev_sec = 0, 0
for i in range(n):
    cur_team, cur_time = input().split()
    m, sec = map(int, cur_time.split(':'))

    win_time = 0
    if i != 0:
        win_time = (m * 60 + sec) - (prev_m * 60 + prev_sec)

    if cur_team == '1':
        if prev_team == cur_team:
            one_win_time += win_time
        else:
            two_win_time = win_time
    else:
        if prev_team == cur_team:
            two_win_time += win_time
        else:
            one_win_time = win_time

    prev_m, prev_sec = m, sec
    if i != n - 1:
        prev_team = cur_team

    # last
last_win_time = (48 * 60) - (prev_m * 60 + prev_sec)
if cur_team == '1':
    if prev_team == cur_team:
        one_win_time += last_win_time
    else:
        two_win_time = last_win_time
else:
    if prev_team == cur_team:
        two_win_time += last_win_time
    else:
        one_win_time = last_win_time

print('{:0>2}:{:0>2}'.format(one_win_time // 60, one_win_time % 60))
print('{:0>2}:{:0>2}'.format(two_win_time // 60, two_win_time % 60))
