s = list(input())

maxVal, minVal = [], []
mCnt = 0 if s[0] == "K" else 1
for i in range(1,len(s)):
    #최대값을 구하기 위한 cnt
    mCnt = mCnt + 1 if s[i] == "M" else mCnt

    #최대값 구하기
    if mCnt == 0 and s[i] == "K":
        maxVal.append("5")
    if mCnt > 0 and s[i] == "K":
        maxVal.append("5" + ("0" * mCnt))
        mCnt = 0
    if mCnt > 0 and len(s) == i+1: #마지막인 경우
        maxVal.append("1")
        mCnt = 0

mCnt = 0
for i in range(len(s)):
    #최소값 구하기
    if s[i] == "K":
        minVal.append("5")
    elif s[i] == "M" and mCnt > 0:
        minVal.append("0")
    elif s[i] == "M":
        minVal.append("1")

print("".join(maxVal))
print("".join(minVal))