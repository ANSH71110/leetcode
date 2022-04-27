class Solution:
    def firstUniqChar(self, s: str) -> int:
        i=0
        d={}
        t=len(s)
        s1=''.join(set(s))
        while i<len(s):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
            i+=1
        i=0
        while i<len(s1):
            if d[s1[i]]==1:
                if s.index(s1[i])<t:
                    t=s.index(s1[i])
            i+=1
        if t<len(s):
            return t
        return -1
