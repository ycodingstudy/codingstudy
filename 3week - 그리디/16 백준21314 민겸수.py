mingum_su = input()

m_cnt = 0
max_res = ""
min_res = ""
for item in mingum_su:
    if item == 'M':
        m_cnt += 1
    else:  # item == 'K'
        if m_cnt == 0:
            max_res += '5'
            min_res += '5'
        else:
            max_res += '5' + '0' * m_cnt
            min_res += '1' + '0' * (m_cnt - 1) + '5'
        m_cnt = 0

# 마지막 m_cnt 처리
if m_cnt != 0:
    max_res += '1' * (m_cnt)
    min_res += '1' + '0' * (m_cnt - 1)

print(max_res)
print(min_res)
