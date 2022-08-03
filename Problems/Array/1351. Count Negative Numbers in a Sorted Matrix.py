class Solution:
    def countNegatives(self, g: List[List[int]]) -> int:
        c=0
        i=0
        while i<len(g):
            j=0
            while j<len(g[i]):
                if g[i][j]<0:
                    c+= len(g[i])-j
                    j=len(g[i])
                j+=1
            i+=1
        return c
