S = list(input())
cnt = {"0": 0, "1": 0}
before = S[0] #0

for i in S:
    if before != i:  # 만약 문자가 이전 문자와 다르다면
        cnt[i] += 1
    before = i

print(cnt[min(cnt)])