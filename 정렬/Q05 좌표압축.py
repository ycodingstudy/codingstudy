n = int(input())
num = list(map(int,input().split()))
sorted_arr = sorted(list(set(num)))
dic = {}

for i in range(len(sorted_arr)):
    dic[sorted_arr[i]] = i

for i in num:
    print(dic[i], end=' ')
