n = int(input())

info = []
for _ in range(n):
    input_data = input().split()
    info.append((input_data[0], int(input_data[1])))

info.sort(key=lambda x: x[1])

for item in info:
    print(item[0], end=' ')
