N = int(input())
switch = list(map(int, input().split()))
switch.insert(0, 0)
S = int(input())
for _ in range(S):
    g, idx = map(int, input().split())
    # 남학생인 경우
    if g == 1:
        for i in range(idx, N + 1, idx):
            switch[i] = abs(switch[i] - 1)
    # 여학생
    else:
        switch[idx] = abs(switch[idx] - 1)
        for i in range(1, N):
            l = idx - i
            r = idx + i
            if r > N or l < 1: break
            if switch[l] == switch[r]:
                switch[r] = abs(switch[r] - 1)
                switch[l] = abs(switch[l] - 1)
            else:
                break
for i in range(1, N + 1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()
