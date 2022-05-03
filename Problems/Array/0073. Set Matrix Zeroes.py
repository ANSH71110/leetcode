class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        i=0
        j=0
        riz=0
        rjz=0
        while i<m:
            j=0
            while j<n:
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
                    if i==0:
                        riz=1
                    if j==0:
                        rjz=1
                j+=1
            i+=1
        i=1
        while i<m:
            j=1
            while j<n:
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
                j+=1
            i+=1
        if riz==1:
            i=0
            j=0
            while j<n:
                matrix[i][j]=0
                j+=1
        if rjz==1:
            i=0
            j=0
            while i<m:
                matrix[i][j]=0
                i+=1
