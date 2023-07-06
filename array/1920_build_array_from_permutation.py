from typing import List


# 1 - method O(n) space
def buildArray(nums: List[int]) -> List[int]:
    return [nums[i] for i in nums]


# 2 - method O(1) space
def buildArray(nums: List[int]) -> List[int]:
    n = len(nums)

    for i in range(n):
        nums[i] += (nums[nums[i]] % n) * n

    for i in range(n):
        nums[i] //= n
        print(nums[i])
        nums[i] = abs(nums[i])

    return nums

print(buildArray([5, 0, 1, 2, 3, 4]))
