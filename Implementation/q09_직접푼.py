input_str = input()

min_len = len(input_str)

for unit in range(1, min_len // 2 + 1):

    result = ""

    previous = input_str[0 : unit]

    count = 1

    for idx in range(unit, min_len, unit):

        now = input_str[idx: idx + unit]

        if (now == previous):
            count += 1

        else: # 이전과 다르다면

            if (count >= 2):
                result += str(count) + previous

            else:
                result += previous

            previous = now
            count = 1

    if count >=2 :
        result += str(count) + previous

    else:
        result += previous

    min_len = min(min_len, len(result))

print(min_len)



