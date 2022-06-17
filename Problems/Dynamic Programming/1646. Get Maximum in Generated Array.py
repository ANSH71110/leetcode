class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        l=[0,1]
        i=2
        while i<=n:
            if i%2==0:
                j=i//2
                l.append(l[j])
            else:
                j=i//2
                l.append(l[j]+l[j+1])
            i+=1
        return max(l[0:n+1])
