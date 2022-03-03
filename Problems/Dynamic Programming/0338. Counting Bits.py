class Solution:
    def countBits(self, n: int) -> List[int]:
        i=0
        l=[]
        while i<=n:
            s=bin(i)
            l.append(s.count("1"))
            i+=1
        return l
