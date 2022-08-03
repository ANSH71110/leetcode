import math 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ar=[[1]*n]*m
        i=1
        while i<m:
            j=1
            while j<n:
                ar[i][j]=ar[i-1][j]+ar[i][j-1]
                j+=1
            i+=1
        return ar[m-1][n-1]
