##Link to the question - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x=len(nums)
        nums.sort()
        i=0
        while i<=x-1 :
            try:
                if nums[i]==nums[i+1]:
                    i+=2
                else:
                    return nums[i]
            except:
                return nums[i]
