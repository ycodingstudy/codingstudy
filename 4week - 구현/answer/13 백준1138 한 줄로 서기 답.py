# [참고 링크] https://gudwns1243.tistory.com/31
# 작은 수부터 자리를 채움. 즉 왼쪽에 큰 사람 수 만큼 자리를 두고 값을 채움

# 2 1 1 0인 경우
# 0 0 1 0
# 0 2 1 0
# 0 2 1 3
# 4 2 1 3

n = int(input())
arr = list(map(int, input().split()))
answer = [0] * n

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == arr[i] and answer[j] == 0:
            answer[j] = i + 1
            break
        elif answer[j] == 0:  # 0을 가장 큰 사람 처럼 취급하는 게 중요한 점
            cnt += 1

print(" ".join(map(str, answer)))
