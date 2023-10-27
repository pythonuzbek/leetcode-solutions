from collections import Counter

nums = [-1,1,-6,4,5,-6,1,4,1]
cnt = Counter(nums)
print(sorted(nums, key=lambda x: (cnt[x], -x)))


