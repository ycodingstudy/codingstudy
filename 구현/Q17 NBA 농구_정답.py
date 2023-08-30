def timeToNum(timeStr):  # "01:10"과 같은 시간 문자열을 초단위의 정수로 바꾼다. (ex. "00:00" -> 0, "10:00" -> 600)
    minute, second = map(int, timeStr.split(":"))
    return minute * 60 + second


def numToTime(num):  # 반대로 초단위의 정수를 시간 문자열로 바꾼다.
    minute = str(num // 60)
    second = str(num % 60)
    if len(minute) == 1:
        minute = "0" + minute
    if len(second) == 1:
        second = "0" + second
    return minute + ":" + second


N = int(input())
scoreDict = {}  # 시간을 key값, 득점한 팀 번호를 value로 한다. (득점 시간이 겹치지 않는다 했으므로)

for i in range(N):
    teamNo, timeStr = input().split()
    scoreDict[timeToNum(timeStr)] = int(teamNo)

teamWinTime1 = 0  # 1번 팀이 이기고 있던 시간
teamWinTime2 = 0  # 2번 팀이 이기고 있던 시간
teamScore1 = 0  # 현재 1번 팀 점수
teamScore2 = 0  # 현재 2번 팀 점수
for i in range(0, timeToNum("48:00")):  # 매 초마다 승자를 체크한다.
    if i in scoreDict:
        if scoreDict[i] == 1:
            teamScore1 += 1
        else:
            teamScore2 += 1

    if teamScore1 > teamScore2:
        teamWinTime1 += 1
    elif teamScore1 < teamScore2:
        teamWinTime2 += 1

print(numToTime(teamWinTime1))
print(numToTime(teamWinTime2))