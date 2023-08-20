# 핵심 아이디어
# 숫자 문자를 먼저 나누고 먼저 문자를 오름차순으로 변환후 마지막에 숫자를 더한 것을 넣어준다.

# K1KA5CB7
import sys

input_str = sys.stdin.readline().rstrip()

str_lst = []
num_lst = []

for s in input_str:
    if  'A' <= s <= 'Z': # 입력은 대문자만 들어오기 때문에 A부터 Z까지의 문자를 담음
        str_lst.append(s)
    else:
        num_lst.append(int(s)) # 숫자를 마지막에 넣어줘야하기때문에 숫자 리스트에 담음

str_lst.sort() # 문자 먼저 정렬 후
str_lst.append(str(sum(num_lst))) # 마지막에 숫자합을 더해서 넣음 str로 변환후 넣음

result = ''.join(str_lst) # 리스트 string으로 변환

print(result)

# str_lst.sort()
#
# str_lst = "".join(str_lst)
#
# print(str_lst)
# a = '1'
# b = '9'
# print(ord(a), ord(b))