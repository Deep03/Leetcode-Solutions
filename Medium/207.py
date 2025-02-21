#287. Find the Duplicate Number
# Brute Force Solution
class Solution:
    def findDuplicate(self, nums: List[int]) -> int: # type: ignore
        for i in range(0, len(nums)):
            count = 1
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count = count - 1
            if count <= 0:
                return nums[i]
        return 0
    
# Optimzed Solution
