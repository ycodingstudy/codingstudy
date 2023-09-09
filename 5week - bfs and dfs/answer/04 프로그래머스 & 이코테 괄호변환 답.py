# DFS의 핵심 개념이 들어간 문제

# 균형잡힌 괄호 문자열의 인덱스 반환
def balanced_index(p):
    count = 0 # 왼쪽 괄호의 수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

# 올바른 괄호 문자열 판단
def check_proper(p):
    count = 0 # 왼쪽 괄호의 수
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0: # 쌍이 맞지 않는 경우
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer

    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]

    if check_proper(p):
        answer = u + solution(v)
    else:
        answer = '(' + solution(p) + ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer