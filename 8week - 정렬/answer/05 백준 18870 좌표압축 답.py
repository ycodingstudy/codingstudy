n = int(input())
nums = list(map(int, input().split()))

set_nums = sorted(nums)
dic = {set_nums[i]: i for i in range(len(set_nums))}

for i in nums:
    print(dic[i], end=' ')