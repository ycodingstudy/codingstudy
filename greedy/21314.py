s = 'MKM'

s = s.replace('KKM', 'K5M')
print(s)

s = s.split('5')

print(s)

max_result = ''
for s1 in s:
    if 'K' in s1 :
        m_cnt = s1.count('M')
        s1 = str(5) + (str(0) * m_cnt)


    else:
        m_cnt = s1.count('M')
        s1 = str(1) + str(0) * m_cnt
    max_result += s1


print(max_result)