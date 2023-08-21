def appendAnswer(cnt):
    answer = ""
    pol = ["AAAA", "BB"]
    if cnt == 0:
        return ""
    while cnt > 0:
        if cnt // 4 > 0:
            answer += pol[0]
            cnt -= 4
        if cnt == 2:
            answer += pol[1]
            cnt -= 2
    return answer

def solution():
    s = input()
    answer = ""
    cnt = 0
    if len(s) < 2:
        return -1
    for i in s:
        if i == ".":
            if cnt % 2 != 0:
                return -1
            else:
                answer += appendAnswer(cnt)
                if len(answer) != len(s):
                    answer += "."
                cnt = 0
        else:
            cnt += 1
    if cnt % 2 == 0:
        answer += appendAnswer(cnt)

    return answer
print(solution())