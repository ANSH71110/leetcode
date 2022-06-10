class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        r=''.join(sorted(r))
        m=''.join(sorted(m))
        i=0
        j=0
        while i<len(m) and j<len(r):
            if m[i]==r[j]:
                j+=1
            i+=1
        if j==len(r):
            return 1
        return 0
