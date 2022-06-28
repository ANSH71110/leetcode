class Solution:
    def nre(self, lt:list, num:int):
        return flag,lt
    def minDeletions(self, s: str) -> int:
        l=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for i in s:
            l[ord(i)-97]+=1
        s=sum(l)
        k=0
        l.sort(reverse=True)
        while k<len(l):
            j=0
            while j<len(l):
                if l[k]==l[j] and l[k]>0 and k!=j:
                    l[k]-=1
                    j=-1
                elif l[k]==0:
                    l.pop(k)
                    k-=1
                    break
                j+=1
            k+=1
            
        return s-sum(l)
