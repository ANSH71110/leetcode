class Solution:
    def addToArrayForm(self, d: List[int], k: int) -> List[int]:
        i=0
        n=0
        while i<len(d):
            n*=10
            n+=d[i]            
            i+=1
        return list(str(n+k))
