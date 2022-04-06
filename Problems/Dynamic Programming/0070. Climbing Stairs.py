class Solution:
    def climbStairs(self, n: int) -> int:
        i=0
        a=1
        b=2
        c=0
        if n==1:
            return a
        elif n==2:
            return b
        else:
            while i<n-2:
                c=a+b
                a=b
                b=c
                i+=1
            return c
