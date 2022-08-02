class Solution:
    def kthSmallest(self, m: List[List[int]], k: int) -> int:
        ar=[]
        i=0
        while i<len(m):
            j=0
            while j<len(m[i]):
                ar.append(m[i][j])
                j+=1
            i+=1
        ar.sort()
        return ar[k-1]
