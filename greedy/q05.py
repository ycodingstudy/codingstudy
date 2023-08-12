n, m =  map(int, input().split())

k_lst = list(map(int, input().split()))

cnt = 0
for i in range(len(k_lst)):
    target = k_lst[i]
    for j in range(i + 1, len(k_lst) ):
        if target == k_lst[j]:
            pass
        else:
            cnt += 1

print(cnt)