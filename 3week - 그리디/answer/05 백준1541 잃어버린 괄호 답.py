arr = input().split('-')

total = 0
for i in arr[0].split('+'):
    total += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        total -= int(j)
print(total)
