arr = sorted(input())

cnt, sum = 0, 0
for i in arr:
    if i.isdecimal():
        sum += int(i)
        cnt += 1
    else:
        break

print(''.join(arr[cnt:]) + str(sum))
