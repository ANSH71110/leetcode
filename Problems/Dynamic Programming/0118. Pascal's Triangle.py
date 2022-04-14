class Solution:
    def generate(self, n: int) -> List[List[int]]:
        i=0
        l=[[1]]
        a=[]
        while i<n-1:            
            j=0
            a.append(1)
            while j<len(l[i])-1:
                a.append(l[i][j]+l[i][j+1])
                j+=1
            a.append(1)
            l.append(a)
            a=[]
            i+=1
        return l
