class Solution:
    def secondHighest(self, s: str) -> int:
        ds=set()
        i=0
        while i<len(s):
            if ord(s[i])<=60:
                ds.add(int(s[i]))
            i+=1
        ds=list(ds)
        if len(ds)<2:
            return -1
        else:
            ds.pop(ds.index(max(ds)))
            return max(ds)
