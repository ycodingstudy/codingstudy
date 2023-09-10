# "균형잡힌 괄호 문자열"의 인덱스 반환
def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1

        if count == 0:
            return i

# "올바른 괄호 문자열"인지 판단
def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0: # 쌍이 맞지 않는 경우에 False 반환
                return False
            count -= 1
    return True #쌍이 맞는 경우에 True



def solution(p):
    answer = ''
    # 1번
    if p =='':
        return answer

    # 2번
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]

    # 3번
    if check_proper(u):
        answer = u + solution(v)

    # 4번 "올바른 괄호 문자열"이 아니라면 아래의 과정을 수행
    else:
        answer = '(' # 4-1
        answer += solution(v) # 4-2
        answer += ')' # 4-3
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer




