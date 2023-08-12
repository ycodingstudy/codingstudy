import sys

n = int(sys.stdin.readline())

coin_lst = list(map(int, sys.stdin.readline().split()))
coin_lst.sort()

result = 0
for i in range(len(coin_lst)):
    if i == 0:
        result += coin_lst[i]
    else:
        target = result + 1
        result += coin_lst[i]
        if target < result:
            print(target)
            break


