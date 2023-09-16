import sys
from itertools import permutations

n = int(sys.stdin.readline())
num_lst = list(map(int, sys.stdin.readline().split()))
operation_lst = list(map(int, sys.stdin.readline().split()))

maximum = -int(1e9)
minimum = int(1e9)

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num_lst[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num_lst[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num_lst[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num_lst[depth]), plus, minus, multiply, divide - 1)

dfs(1, num_lst[0], operation_lst[0], operation_lst[1], operation_lst[2], operation_lst[3])
print(maximum)
print(minimum)



