class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        i=1
        while i<len(t):
            t[i][0]+=t[i-1][0]
            t[i][-1]+=t[i-1][-1]
            i+=1
        i=2
        while i<len(t):
            j=1
            while j<i:
                t[i][j]+=min(t[i-1][j],t[i-1][j-1])
                j+=1
            i+=1
        return min(t[-1])
