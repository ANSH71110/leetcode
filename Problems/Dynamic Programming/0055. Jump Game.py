class Solution:
    def canJump(self, n: List[int]) -> bool:
        g,i=len(n)-1,len(n)-2
        if i<0:
            return 1
        while i>=0:
            if n[i]+i>=g:
                g=i
            i-=1
            
        if g==0:
            return 1
        return 0
