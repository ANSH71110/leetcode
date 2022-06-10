class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        l=list(number)
        i=0
        g=[]
        while i<len(l):
            if l[i]==digit:
                l.pop(i)
                g.append(int("".join(l)))
                l=list(number)
            i+=1
        return str(max(g))
