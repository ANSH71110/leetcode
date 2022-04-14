class Solution:
    def getRow(self, n: int) -> List[int]:
        i=0
        l=[[1]]
        a=[]
        while i<n:            
            j=0
            a.append(1)
            while j<len(l[0])-1:
                a.append(l[0][j]+l[0][j+1])
                j+=1
            a.append(1)
            l=[]
            l.append(a)
            a=[]
            i+=1
        return l[-1]
