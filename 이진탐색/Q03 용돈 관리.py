n, m = map(int,input().split())
arr = [int(input()) for _ in range(n)]
start, end = min(arr), sum(arr)
result = 0
while start <= end:
    mid = (start+end) // 2
    cnt = 1
    current = mid
    for k in arr:
        if current < k:
            current = mid
            cnt +=1
        current -= k

    if cnt < m:
        end = mid-1
    else:
        start = mid + 1
        result = mid
print(result)