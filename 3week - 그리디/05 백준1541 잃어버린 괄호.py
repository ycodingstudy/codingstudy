expression = input()
expression_length = len(expression)

stack_list = []
minus_cnt = 0
bracket = []
j = 0
for i in range(expression_length):
    if expression[i] == '+':
        if minus_cnt == 0:
            stack_list.append(int(expression[j:i]))
            j = i + 1
        else:  # minus_cnt is 1
            bracket.append(int(expression[j:i]))
            j = i + 1
    elif expression[i] == '-':
        if minus_cnt == 0:
            stack_list.append(int(expression[j:i]))
            j = i + 1
            minus_cnt += 1
        else:  # minus_cnt is 1
            bracket.append(int(expression[j:i]))
            stack_list.append(-sum(bracket))
            j = i + 1
            bracket = []
            minus_cnt = 0
    else:
        continue
    if minus_cnt == 1 and i == expression_length - 1:
        bracket.append(int(expression[j:i]))
        stack_list.append(-sum(bracket))
        # j = i (but 하지만 전부 끝남!
        # minus_cnt = 0

print(sum(stack_list))
print(bracket)

