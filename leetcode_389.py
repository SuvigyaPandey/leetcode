##Link of the question - https://leetcode.com/problems/find-the-difference/


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        s = sorted(s)
        t = sorted(t)
        i = 0
        while True:
            try:
                if s[i] == t[i]:
                    i+=1
                else:
                    return t[i]
            except:
                return t[i]
