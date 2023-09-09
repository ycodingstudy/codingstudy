def solution(p):
    if len(p) == 0 or correctBracket(p):  # 1 빈 문자열이거나 올바른 문자열
        print(p)
        return p
    u, v = splitBracket(p)  # 2 균형잡힌 괄호 문자열로 분리
    print(u, v)
    if correctBracket(u):  # 3 올바른 괄호 문자열이라면
        return u + solution(v)  # v에 대해 1단계부터 다시 수행(결과 문자열을 u에 이어 붙인다)
    else:  # 4 u가 올바른 문자열이 아니라면
        answer = "("  # 4-1 첫번째문자
        answer += solution(v)  # 4-2 다시 1단계부터 수행하고 문자열 이어 붙이기
        answer += ")"  # 4-3

        for pp in u[1:len(u) - 1]:  # 4-4 첫 번째 문자와 마지막 문자를 제거
            if pp == "(":  # 4-4 나머지 문자열 괄호를 뒤집기
                answer += ")"
            else:
                answer += "("
        return answer  # 생성된 문자열 반환


def balanceBracket(st):
    cnt = 0
    for s in st:
        cnt = -1 if cnt == ")" else 0
    return cnt == 0


def correctBracket(st):
    if balanceBracket(st) == False or st[0] == ")" or st[-1] == "(":
        return False

    dic = {"(": 0, ")": 0}
    for s in st:
        dic[s] += 1
        if dic["("] < dic[")"]:
            return False
    return True


def splitBracket(st):
    dic = {"(": 0, ")": 0}
    for i, s in enumerate(st):
        dic[s] += 1
        if dic["("] == dic[")"]:
            return st[:i + 1], st[i + 1:]