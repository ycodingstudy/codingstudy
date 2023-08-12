num_str1 =  list(map(int, input()))
num_str2 = num_str1.copy()

cnt1 = 0
cnt2 = 0
for i in range(len(num_str1)):
    if num_str1[i] == 0 :
        tmp = i
        while num_str1[tmp] != 1 and tmp != len(num_str1) - 1 :
            num_str1[tmp] = 1
            tmp += 1

        cnt1 += 1

for j in range(len(num_str2)):
    if num_str2[j] == 1 :
        tmp = j
        while num_str2[tmp] != 0 and tmp != len(num_str1) - 1:
            num_str2[tmp] = 0
            tmp += 1
        cnt2 += 1

print(min(cnt1, cnt2))