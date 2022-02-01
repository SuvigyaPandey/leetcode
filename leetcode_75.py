
#Link to question - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums = [2,0,2,1,1,0]
        #.    0->red, 1->white, 2->blue
        # sort this in order -> "similar colors are adjacent "
        # output ->[0,0,1,1,2,2]
        
        l,r=0,len(nums)-1
        i = 0 #pivot
        
        def swap(i,j):
            
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
            
        while i <=r:
            if nums[i]==0:
                swap(l,i)
                l +=1
            elif nums[i]==2:
                swap(i,r)
                r -=1
                i-=1
            i +=1
                
                   
        

