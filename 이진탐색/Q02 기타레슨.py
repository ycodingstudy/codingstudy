n, m = map(int,input().split())
arr = list(map(int,input().split()))

result, start, end = 0, max(arr), sum(arr)
while start <= end:
    mid = (start + end) // 2

    #블루레이에 강의 넣기
    cnt, total = 0,0
    for i in range(n):
        if total + arr[i] > mid:
            cnt +=1
            total = 0
        total += arr[i]

    if total > 0:
        cnt += 1

    if cnt > m:
        start = mid +1
    else:
        end = mid - 1
        result = mid

print(result)