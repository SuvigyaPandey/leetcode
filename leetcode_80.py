#Link for the question - https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<3:
            return len(nums)
        i = 2
        while i<len(nums):
            if nums[i]==nums[i-2]:
                nums.pop(i)
            else:
                i+=1
        return len(nums)
