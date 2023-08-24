# https://www.acmicpc.net/problem/1541

expression = input().strip()
operands = expression.split('-')

# 첫 번째 연산자 이전까지의 숫자들은 더하기
total = sum(map(int, operands[0].split('+')))

for operand in operands[1:]:
    total -= sum(map(int, operand.split('+')))

print(total)