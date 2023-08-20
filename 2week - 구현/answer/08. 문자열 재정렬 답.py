data = input()
result = []
value = 0

# 문자 하나씩 확인
for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()  # 알파벳 오름 차순 정렬

if value != 0:
    result.append(str(value))

print("".join(result))
