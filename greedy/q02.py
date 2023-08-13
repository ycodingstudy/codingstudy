num_str = input()

len_num_str = len(num_str)

if len_num_str == 1:
    result = int(num_str)

else: #12, 234
    result = max( int(num_str[0])  + int(num_str[1]) , int(num_str[0])  * int(num_str[1])  )

    for idx in range(1, len_num_str - 1):
        result = max( result + int(num_str[idx + 1]) , result * int(num_str[idx + 1]) )

print(result)