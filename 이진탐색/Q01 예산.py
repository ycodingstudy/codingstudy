n = int(input())
arr = list(map(int,input().split()))
total = int(input())
start, result, end = 0, max(arr), max(arr)

while start <= end:
    mid = (start + end) // 2
    temp_total = 0
    for i in arr:
        if i >= mid:
            temp_total += mid
        else:
            temp_total += i

    if temp_total <= total:
        start = mid+1
    else:
        end = mid - 1
        result = end

print(result)
