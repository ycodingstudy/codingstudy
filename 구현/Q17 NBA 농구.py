def getSeconds(s):
    minute, seconds = map(int, s.split(":"))
    return seconds + minute * 60

def getTime(s):
    minute = str(s // 60)
    if len(minute) == 1:
        minute = "0" + minute
    seconds = str(s % 60)
    if len(seconds) == 1:
        seconds = "0" + seconds
    return minute + ":" + seconds

N = int(input())
total = 2880  # 48분
result = {"1": 0, "2": 0}
team, time = map(str, input().split())
cnt = 1 if team == "1" else -1
before = getSeconds(time)
bteam = team
for _ in range(1, N):
    team, time = map(str, input().split())
    cnt = cnt + 1 if team == "1" else cnt - 1

    if cnt == 0:
        result[str((int(team) % 2) + 1)] += getSeconds(time) - before
        before = 0
    elif bteam != team and cnt != 0:
        if team == "1" and cnt > 0 or team == "2" and cnt < 0:
            before = getSeconds(time)
            bteam = team

result[team] += total - getSeconds(time)

print(getTime(result['1']))
print(getTime(result['2']))