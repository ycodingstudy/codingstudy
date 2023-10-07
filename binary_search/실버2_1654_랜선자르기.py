import sys
k, n = map(int, sys.stdin.readline().split())

lanCable = []
for _ in range(k):
    lanCable.append(int(sys.stdin.readline()))

start = 1
end = max(lanCable)

while start <= end:
    mid = (start + end) // 2

    result = 0
    for cable in lanCable:
        result += cable // mid

    if result >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)