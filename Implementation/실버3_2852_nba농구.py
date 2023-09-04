import sys

def convert_second_to_minute_second(second):
    result = ':'
    minute = (second // 60)
    second = second - (minute * 60)
    if minute < 10:
        minute = '0' + str(minute)
    else:
        minute = str(minute)

    if second < 10:
        second = '0' + str(second)
    else:
        second = str(second)
    result = minute + result + second

    return result

def convert_minute_second_to_second(minute_second):
    minute = int(minute_second[:2])
    sec =  minute * 60 + int(minute_second[3:5])
    return sec

n = int(input())
lst = []
a_team_goal = 0 # 1번팀 골
b_team_goal = 0 # 2번팀 골
for i in range(n):
    tmp = list(sys.stdin.readline().split())
    if tmp[0] == '1':
        a_team_goal += 1 # 1번팀 골
    else:
        b_team_goal += 1 # 2번팀 골
    lst.append(tmp)

lst.append(['0', '48:00'])
# 사전 준비 끝


a_team_win_time = 0
b_team_win_time = 0

for i in range(n, 0, -1):
    if a_team_goal == b_team_goal:
        pass

    elif a_team_goal > b_team_goal:
        a_team_win_time += convert_minute_second_to_second(lst[i][1]) - convert_minute_second_to_second(lst[i-1][1])

    elif a_team_goal < b_team_goal:
        b_team_win_time += convert_minute_second_to_second(lst[i][1])  - convert_minute_second_to_second(lst[i-1][1])

    if lst[i-1][0] == '1':
        a_team_goal -= 1

    elif lst[i-1][0] == '2':
        b_team_goal -= 1


print(convert_second_to_minute_second(a_team_win_time))
print(convert_second_to_minute_second(b_team_win_time))

