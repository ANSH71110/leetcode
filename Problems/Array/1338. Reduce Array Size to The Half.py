import collections
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        s=list(set(arr))
        if len(s)==len(arr):
            return len(arr)//2
        i=0
        l=[]
        while i<len(s):
            l.append(arr.count(s[i]))
            i+=1
        c=0
        i=len(arr)//2
        while i>0:
            j=l.index(max(l))
            i-=l[j]
            l[j]=0
            c+=1
        return c
