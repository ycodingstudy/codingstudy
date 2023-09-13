import sys;
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())# + - * /

maxNum = -int(1e9)
minNum = int(1e9)


def dfs(add, sub, mul, div, total, i):
    global maxNum, minNum
    if i == n:
        maxNum = max(maxNum, total)
        minNum = min(minNum, total)
        return
    if add:
      dfs(add-1, sub, mul, div, total + numbers[i], i+1)
    if sub:
      dfs(add, sub-1, mul, div, total - numbers[i], i+1)
    if mul:
      dfs(add, sub, mul-1, div, total * numbers[i], i+1)
    if div:
      dfs(add, sub, mul, div-1, int(total / numbers[i]), i+1)

dfs(add, sub, mul, div, numbers[0], 1)
print(maxNum)
print(minNum)