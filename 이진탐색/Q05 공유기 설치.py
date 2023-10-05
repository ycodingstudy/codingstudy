n, c = map(int,input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

start = 1
end = arr[-1] - arr[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    current = arr[0]

    for i in range(1,n):
        if arr[i] - current >= mid:
            cnt+=1
            current = arr[i]

    if cnt >= c:
        if result < mid:
            result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)