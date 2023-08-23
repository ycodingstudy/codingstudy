# 연속하는 색끼리 묶음을 만든다.
# BB / R / B / R / BB
# B 묶음은 3개 R 묶음은 2개가 된다
# 묶음이 더 많은 B로 전체를 칠하고, R을 부분을 칠해주면 된다
# 전체 B 1번에 R 2묶음 2번을 더해서 총 3번

n = int(input())
colors = input()

red_by_b_split = colors.split('B')
# print("red : ", red_by_b_split)
red = list(filter(None, red_by_b_split))
print(red)


blue_by_r_split = colors.split('R')
# print("blue : ", blue_by_r_split)
blue = list(filter(None, blue_by_r_split))

cnt = 1 + min(len(red), len(blue))
print(cnt)