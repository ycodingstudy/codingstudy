s1 = input()

s1 = s1.replace('XXXX', 'AAAA')
s1 = s1.replace('XX', 'BB')

if 'X' in s1:
    print(-1)
else:
    print(s1)


