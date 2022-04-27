import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c<=1:
            return 1
        j=int(sqrt(c))
        i=0
        while i<=j:
            p=(i*i)+(j*j)
            if p>c:
                j-=1
            elif p<c:
                i+=1
            else:
                return 1
        return 0
