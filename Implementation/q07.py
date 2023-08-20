# https://www.acmicpc.net/problem/18406 브론즈2
# 풀이시간 : 약 20분

# 풀었던 핵심 아이디어 :
# 1) 반으로 나누고
# 2) 합하고
# 3) 비교한다

input_str = input() # 입력

input_str_halflen = len(input_str)//2 # 입력글자의 길이를 반으로 나눔

first_str = input_str[:input_str_halflen] # 반으로 나눈 첫번째 str
second_str = input_str[input_str_halflen:] # 반으로 나눈 두번째 str

first_result = 0
for s in first_str: # 첫번째 str 값을 더함
    first_result += int(s)

second_result = 0
for s in second_str: # 두번째 str 값을 더함
    second_result += int(s)

if first_result == second_result: # 첫번째 str 합과 두번째 str 합을 비교해서
    print("LUCKY") # 맞으면 LUCKY

else:  # 틀리면 READY
    print("READY")