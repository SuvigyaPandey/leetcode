## Link to question - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap={}
        
        for i,n in enumerate(numbers):
            
            diff=target-n
            
            if diff in hashMap:
                
                return sorted([i+1,hashMap[diff]+1])
            hashMap[n]=i
            
            
