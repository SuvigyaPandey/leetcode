##Link of the question - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(l,r):
            m = (l+r) // 2
            
            if l>r:
                return None

            root_node=TreeNode(nums[m])
            root_node.left= helper(l,m-1)
            root_node.right = helper(m+1,r)
            return root_node
        return helper(0,len(nums)-1)
