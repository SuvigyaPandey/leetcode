##Link of the question - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        res=""
        carry=0
        
        a=a[::-1]
        b=b[::-1]
        for i in range(max(len(a),len(b))):
            D_A=int(a[i]) if i< len(a) else 0
            D_B= int(b[i]) if i<len(b) else 0
            
            total = D_A+D_B+carry
            char=str(total%2)
            res=char+res
            
            carry=total//2
            
        if carry:
            res="1"+res
        return res

