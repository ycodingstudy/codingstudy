# aabbaccc의 경우 2a2ba3c 로 압축
# ababcdcdababcdcd 의 경우 1개 단위로 하면 압축 불가
# 2개 단위로 끊어서 2ab2cd2ab2cd로 표현 가능
# 8개 단위로 끊으면 2ababcdcd로 표현 (가장 짧은 표현법)
# 가장 짧은 것의 길이를 return하게 할 것



s = input()  # aabbaccc
s_len = len(s)  # 8

len_list = []
for i in range(1, s_len + 1):  # i : cut 단위
    res = ''
    cnt = 1
    cut_s = s[:i]  # i : 1, a
    # python의 문자열은 범위를 벗어나서 출력하면 ''으로 나옴
    for j in range(i, s_len + i, i):  # 잘리는 길이 i처음 부터 i까지씩 한 번에 보는데
        if cut_s == s[j:j + i]:  # 기존의 값과 다음 값(i 만큼)
            cnt += 1
        else:  # 다르면 기존의 것을 문자열로 연결
            if cnt > 1:
                res = res + str(cnt) + cut_s  # 2a
            else:
                res = res + cut_s
            cnt = 1 # 다음을 위한 초기화
            cut_s = s[j: j + i]

    len_list.append(len(res))

print(min(len_list))
