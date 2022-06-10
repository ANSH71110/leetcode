class Solution:
    def countEven(self, n: int) -> int:
        j=1
        c=0
        while j<=n:
            i=j
            if i>9:
                s=0
                while i>0:                    
                    s+=i%10
                    i//=10
                i=s      
            if i%2==0:
                c+=1
            j+=1
        return c
