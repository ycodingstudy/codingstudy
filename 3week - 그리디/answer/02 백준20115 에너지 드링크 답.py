n = int(input())

drink = list(map(int, input().split()))

drink.sort(reverse=True)
sum = drink[0]

for i in range(1, n):
    sum += drink[i] / 2

print('%g' % sum)  # %g 포매팅
