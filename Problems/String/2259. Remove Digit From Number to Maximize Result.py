class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        l=list(number)
        i=0
        g=0
        while i<len(l):
            if l[i]==digit:
                l.pop(i)
                g=max(g,int("".join(l)))
                l=list(number)
            i+=1
        return str(g)
