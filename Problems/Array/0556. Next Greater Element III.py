class Solution:
    def nextGreaterElement(self, n: int) -> int:
        d=list(str(n))
        
        i=j=len(d)-1
        
        while i and d[i]<=d[i-1]:
            i-=1
        
        if i==0:
            return -1
        
        while d[j]<=d[i-1]:
            j-=1

        d[j],d[i-1]=d[i-1],d[j]
        
        d[i:]=d[i:][::-1]
        
        r=int(''.join(d))
        
        if r > 2**31 -1:
            return -1
        else:
            return r
