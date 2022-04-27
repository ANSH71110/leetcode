class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t=''.join(sorted(t))
        s=''.join(sorted(s))
        i=0
        while i<len(s):
            if s[i]!=t[i]:
                return t[i]
            i+=1
        return t[i]
