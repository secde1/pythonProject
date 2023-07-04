# 2553

# nums = [13,25,83,77]

# print([int(c) for n in nums for c in str(n)])

# l = []
# res = "".join([str(i) for i in nums])
# print(res)
# for i in res:
#     l.append(int(i))
# print(l)


# 1725





# 2108
# words = ["abc","car","ada","racecar","cool"]
'''
for i in words:
    if i == i[::-1]:
        print(i)
        break
print("")
'''


# 2733

# nums = [3,2,1,4]
'''
nums.sort()
if len(nums) < 3:
    print('-1')
else:
    print(nums[1])
'''

# 1252 https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/









# 2215
# nums1 = [1,2,3,3]
# nums2 = [1,1,2,2]


# 1827
nums = [1,5,2,4,1]

n = len(nums)
dp = [float('inf')] * n
dp[0] = 0

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = min(dp[i], dp[j] + nums[i] - nums[j])

print(sum(dp))



