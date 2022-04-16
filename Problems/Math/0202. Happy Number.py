class Solution:
    def isHappy(self, n: int) -> bool:
        l=[]      
        while n>1:
            if n in l:
                return 0
            else:
                l.append(n)
            t=0
            while n>0:
                t+=pow(n%10,2)
                n=n//10
            n=t
            #print(n,t)
        if n==1:
            return 1
        else:
            return 0
