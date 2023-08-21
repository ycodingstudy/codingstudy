def solution(s):
    answer = len(s)
    for step in range(1, len(s)):
        comp = ""
        prev = s[0:step]
        count = 1

        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                count +=1
            else:
                comp += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1
        comp += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(comp))
    return answer
            
        