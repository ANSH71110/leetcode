# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        d=0
        l=1
        m=n//2
        if n>1:
            while d!=1:
                val=guess(m)
                if val==0:
                    d=1
                    return m
                elif val==-1:
                    n=m
                    m=(l+n)//2 
                else:
                    l=m
                    m=(l+n)//2
                    if l==m:
                        d=1
                        return n
        else:
            return n
                
