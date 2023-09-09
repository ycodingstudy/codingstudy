def isCorrect(chars):
    stack = []
    for ch in chars:
        if ch == '(':
            stack.append(ch)
        elif stack:
            stack.pop()
        else:
            return False
    return True if len(stack) == 0 else False


def separate(chars):
    lcnt, rcnt = 0, 0
    for i, ch in enumerate(chars):
        if ch == '(':
            lcnt += 1
        else:
            rcnt += 1
        if lcnt == rcnt:
            return chars[:i + 1], chars[i + 1:]
    return chars, ''


def solution(w):
    answer = ''
    if w == '': return ''

    u, v = separate(w)
    if isCorrect(u):
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        for ch in u[1:-1]:
            if ch == '(':
                answer += ')'
            else:
                answer += '('
    return answer


a = solution('()))((()')
print(a)
#  Test case
# (()())()      (()())()
# )(             ()
# ()))((()        ()(())()
