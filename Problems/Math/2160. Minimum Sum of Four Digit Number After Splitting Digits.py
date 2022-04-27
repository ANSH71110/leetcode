class Solution:
    def minimumSum(self, num: int) -> int:
        l=[]
        for i in str(num):
            if int(i)>0:
                l.append(int(i))
        #print(l)
        n=len(l)
        s=0
        if n<=2:
            return sum(l)
        elif n==3:
            s=min(l)
            l.pop(l.index(s))
            s*=10
        else:
            s=10*min(l)
            l.pop(l.index(min(l)))
            s+=10*min(l)
            l.pop(l.index(min(l)))
        return s+sum(l)
            
