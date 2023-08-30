# n명의 사람들(키는 1부터 n까지로 모두 다름)
# 자기보다 큰 사람이 왼쪽에 몇 명 있었는지만을 기억함

n = int(input())  # n : 10 이하의 자연수
infos = list(map(int, input().split()))  # 키 순으로 자기보다 왼쪽 사람의 정보
res = [0] * n
for i in range(n - 1, -1, -1):  # 키 큰 사람부터 진행
    info = infos[i]
    person = i + 1

    cnt = 0
    for j in range(n):
        if cnt == info:
            res.insert(j, person)
            if res[j + 1] == 0:
                del res[j + 1]
            break
        if res[j] > person:
            cnt += 1

# 남아있는 0가 있다면 삭제 후, 출력
for _ in range(res.count(0)):
    res.remove(0)
print(" ".join(map(str, res)))

# 33분 45.65초
