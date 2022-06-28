class Solution:
    def minimumDeletions(self, l: List[int]) -> int:
        mini=l.index(min(l))
        maxi=l.index(max(l))
        n=len(l)
        s=2*n
        s=min(s,max(maxi+1,mini+1),n-maxi+mini+1,n-mini+maxi+1,max(n-mini,n-maxi))
        return s
