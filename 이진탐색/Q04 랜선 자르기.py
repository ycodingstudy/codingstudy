k, n = map(int,input().split())
arr = [int(input()) for _ in range(k)]
start, end, result = 1, max(arr), 0

while start <= end:
    mid = (start+end) // 2
    cnt = 0
    for i in arr:
        cnt += i // mid

    if cnt < n:
        end = mid-1
    else:
        result = mid
        start = mid + 1

print(result)
