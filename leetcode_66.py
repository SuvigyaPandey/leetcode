##Link of the question - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        
        # reverse the list
        
        digits=digits[::-1]
        
        carry=1
        i=0
        
        while carry:
            
            if i<len(digits):
            
                if digits[i]==9:
                    digits[i]=0
                else:
                    digits[i] = digits[i]+1
                    carry=0
            else:
                digits.append(1)
                carry=0
            i +=1
        return digits[::-1]
