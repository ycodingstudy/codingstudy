# 길이가 n인 문자열이 입력되었다면 1에서 n/2까지 모든 수를 단위로 해서 문자열 압축 방법 확인
# 그 중 가장 짧게 압축 되는 길이를 출력

def solution(s):
    answer = len(s)
    # 1개 단위(step) 부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]  # 앞에서 부터 step 만틈의 문자열 추출
        count = 1
        # 단위(step) 크기 만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다음 글자로 넘어가게 업데이트
                count = 1 # cnt 초기화
        # 남아 있는 문자열 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed)) # 매 step 마다 answer의 길이 확인
    return answer