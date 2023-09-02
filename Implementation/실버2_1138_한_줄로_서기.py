import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

result = []
for i in range(n - 1, -1, -1):
    result.insert(lst[i], i + 1)

for i in range(n):
    print(result[i], end = ' ')