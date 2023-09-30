import sys
n = int(sys.stdin.readline())

num_lst = list(map(int, sys.stdin.readline().split()))
num_lst.sort()


if n % 2 == 0:
    median_idx = n // 2 - 1
else:
    median_idx = n // 2

print(num_lst[median_idx])
