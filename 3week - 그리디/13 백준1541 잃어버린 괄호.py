expression = input().split('-')
# print(expression)

sub_total = []
is_start_minus = False
for i in range(len(expression)):
    expr = expression[i].split('+')

    total = 0
    for num in expr:
        if num == '' and i == 0:
            is_start_minus = True
        else:
            total += int(num)
    sub_total.append(total)
# print(sub_total)

if is_start_minus:
    result = -sub_total[0]
else:
    result = sub_total[0]

for i in range(1, len(sub_total)):
    result -= sub_total[i]
print(result)


# -1-1-1