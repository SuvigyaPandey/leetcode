#link of the question - https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(len(nums)):
            n += (i-nums[i])
        return n
                
