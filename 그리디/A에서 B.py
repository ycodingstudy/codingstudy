# https://www.acmicpc.net/problem/16953

num , target = map(int, input().split())
arr = [num]
cnt = 0

#2. while을 돌면서 가장 작은 수가 target 보다 클때 까지
while True:
    temp = []
    cnt += 1
    for i in arr:
        temp.append(i * 2)
        temp.append(int(str(i)+"1"))
    arr = list(set(temp))
    print(min(arr))
    if target in arr:
        break
    if min(arr) >= target:
        cnt = -2
        break
print(cnt+1)