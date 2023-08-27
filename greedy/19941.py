# 아이디어
# 사람은 왼쪽에서 가장 먼 햄버거부터 찾는다(만약 없다면 가장 가까운 왼쪽꺼로 간다)
# 그리고 그것마저 없다면 오른쪽에서 가장 가까운 햄버거를 찾는다
import sys

n, k = map(int, sys.stdin.readline().split())
s = list(sys.stdin.readline().rstrip())

cnt = 0
for i in range(len(s)): # string을 하나씩 다 돌음
    if s[i] == 'P': # 만약 i번째가 사람이라면
        flag = 0
        for j in range(k, 0, -1): # 왼쪽부터 탐색
            if i - j >= 0 and i - j <= n - 1 : # out of range 때문에 범위 지정
                if s[i - j] == 'H':
                    s[i - j] = 'C' # 햄버거를 먹은걸로 바꿔줌
                    cnt += 1
                    flag = 1
                    break

        for j in range(1, k + 1):
            if flag == 1:
                break
            if i + j >= 0 and i + j <= n - 1:
                if s[i + j] == 'H':
                    s[i + j] = 'C' # 햄버거를 먹은 걸로 바꿔줌
                    cnt += 1
                    break

print(cnt)




