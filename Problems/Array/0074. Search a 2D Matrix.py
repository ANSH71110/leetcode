class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        tag=0
        while i<len(matrix):
            if target==matrix[i][-1]:
                return 1
            elif target<matrix[i][-1]:
                tag=1
                break
            i+=1
        j=0
        while tag==1 and j<len(matrix[i]):
            if target==matrix[i][j]:
                return 1
            j+=1
        return 0
