# n 개의 수열과 n-1개의 사칙연산자
# 주어진 수의 순서 바꾸기 X
# 연산자 우선 순위 무시하고 앞에서부터, 나눗셈은 (//)으로
# 목적 : 식의 결과가 최대, 최소 인 것
# oper = ['+', '-', '*', '//']

n = int(input())
num = list(map(int, input().split()))  # [3, 4, 5]
op = list(map(int, input().split()))  # [1, 0, 1, 0] visited


def calculate(x, y, i):
    if i == 0:
        return x + y
    elif i == 1:
        return x - y
    elif i == 2:
        return x * y
    else:  # i == 3
        if y == 0:  # 0나누기
            return 0
        if x < 0:   # 음수 나누기
            return -((-x) // y)
        else: # 양수 나누기
            return x // y


lst = []

def dfs(prev_res, num_idx, oper):  # 최초로 넣을 때 num[0], 1로 시작
    if num_idx == n:
        lst.append(prev_res)
        return

    for i in range(4):# 2) 이웃 노드 중
        if oper[i] > 0:  # 방문이 가능 하면
            oper[i] -= 1  # 방문처리를 하고
            tmp = calculate(prev_res, num[num_idx], i)
            dfs(tmp, num_idx + 1, oper)  # 다시 돈다.
            oper[i] += 1 # 백트레킹


dfs(num[0], 1, op)
print(max(lst))
print(min(lst))

# 소요 시간 : 1:30 정도 보고 다음날..
