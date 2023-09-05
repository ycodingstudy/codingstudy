def toSecond(goal_time):
    m, s = goal_time.split(":")
    sec = int(m) * 60 + int(s)
    return sec


def toStr(time):
    m = time // 60
    s = time % 60
    res = str(m) + ":" if m >= 10 else "0" + str(m) + ":"
    res += str(s) if s >= 10 else "0" + str(s)
    return res


win = {"1": 0, "2": 0}
win_time1, win_time2 = 0, 0
n = int(input())
prev = 0
prev_goal = None
for i in range(n):
    goal, t = input().split()
    cur = toSecond(t)
    win[goal] += 1

    if win["1"] > win["2"]:
        current_goal = "1"
    elif win["1"] < win["2"]:
        current_goal = "2"
    else:
        current_goal = None

    if prev_goal == "1":
        win_time1 += cur - prev
    elif prev_goal == "2":
        win_time2 += cur - prev

    prev = cur
    prev_goal = current_goal

# 게임이 끝난 후
if prev_goal == "1":
    win_time1 += 48 * 60 - prev
elif prev_goal == "2":
    win_time2 += 48 * 60 - prev

print(toStr(win_time1))
print(toStr(win_time2))
