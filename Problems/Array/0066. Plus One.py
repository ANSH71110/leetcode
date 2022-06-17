class Solution:
    def plusOne(self, d: List[int]) -> List[int]:
        i=0
        n=0
        while i<len(d):
            n*=10
            n+=d[i]            
            i+=1
        return [int(i) for i in str(n+1)]
