H, W = map(int, input().split())
answer = []
for i in range(H):
    town = list(input())
    temp = []
    cnt = 0
    temp.append(0 if town[0] == "c" else -1)
    for i in range(1,W):
        if town[i] == "c":
            temp.append(0)
        elif temp[i-1] >= 0:
            temp.append(temp[i-1]+1)
        else:
            temp.append(-1)
    answer.append(temp)

for row in answer:
    print(" ".join(map(str, row)))


