# 캐릭터 점수를 N이라 할 때,
# 자릿수 기준으로 점수 N을 반으로 나누어
# 왼쪽 부분의 자릿수 합과 오른쪽 부분의 각 자릿수 합을 더한 값이 동일

# 123,402
# 좌 : 1 + 2 + 3 = 6, 우 : 4 + 0 + 2 = 6 -> 스킬 사용 가능("LUCKY"), 불가("READY)

n = input()  # 123402를 string으로 받아서
scores = []
for item in n:
    scores.append(int(item))  # 개별적으로 int로 값을 받음

mid_idx = len(scores) / 2 - 1 # 중간 인덱스 미리 계산
left, right = 0, 0
idx = 0
for score in scores:
    if idx <= mid_idx:
        left += score
    else:
        right += score
    idx += 1

if left == right:
    print("LUCKY")
else:
    print("READY")