# 알파벳 대문자, 숫자 0-9의 문자열이 입력됨
# 오름차순 정렬 출력 후, 모든 숫자 값을 이어서 출력

input_str = input()
total = 0
result = []
for item in input_str:
    if item in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        total += int(item)
    else:
        result.append(item)

result.sort()
result.append(str(total)) # ['A', 'B', 'C', 'K', 'K', '13' ]
print(''.join(i for i in result))