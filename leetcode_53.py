##Link to question- https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum=nums[0]
        current_sum= 0
        
        for i in nums:
            if current_sum<0:
                current_sum=0
            current_sum += i
            
            maximum =max(maximum,current_sum)
        return maximum
