class Solution:
    def maxProfit(self, p: List[int]) -> int:
        i=1
        tag=0
        while i<len(p):
            if p[i]>p[0]:
                tag=1
                break
            else:
                p.pop(i-1)
        if len(p)==0:
            return 0
        ar=[]
        def smp(l):
            if len(l)>1:
                if l.index(max(l))<l.index(min(l)):
                    smp(l[0:l.index(max(l))+1])
                    smp(l[l.index(max(l))+1:])
                else:
                    ar.append(max(l)-min(l))
            else:
                ar.append(0)
        smp(p)
        return max(ar)
