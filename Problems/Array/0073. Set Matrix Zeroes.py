class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        i=0
        j=0
        r=set()
        c=set()
        while i<m:
            j=0
            while j<n:
                if matrix[i][j]==0:
                    r.add(i)
                    c.add(j)
                j+=1
            i+=1
        i=0
        while i<m:
            j=0
            while j<n:
                if i in r or j in c:
                    matrix[i][j]=0
                j+=1
            i+=1
