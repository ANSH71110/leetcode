# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        d=0
        l=0
        m=n//2 + 1
        while d!=1:
            if isBadVersion(m):
                n=m
                m=(l+n)//2
                if m==l:
                    d=1
                    return n
            else:
                l=m
                m=(l+n)//2
                if m==l:
                    d=1
                    return n
        
