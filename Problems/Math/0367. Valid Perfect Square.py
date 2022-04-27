class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=1
        while num/i>=i:        
            if num/i==i:
                return 1
            i+=1
        return 0
