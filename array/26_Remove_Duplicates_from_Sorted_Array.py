from typing import List
def removeDuplicates(self, nums: List[int]) -> int:
    s = set(nums)
    for i in s:
        nums.append(i)
    nums.sort()
    return len(nums)