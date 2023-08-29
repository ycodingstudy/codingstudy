input()
drinks = sorted(list(map(int,input().split())), reverse=True)
answer = drinks.pop(0)
for i in drinks:
    answer += i / 2

print('%g'%answer)