class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=1
        j=num
        while i<=j:     
            m=(i+j)//2
            s=m*m
            if s>num:
                j=m-1
            elif s<num:
                i=m+1
            else:
                return 1
        return 0
