class Solution:
    def convert(self, s: str, n: int) -> str:
        l=['']*n
        i=0
        j=0
        tag=1
        while tag<2:
            if tag==1:
                j=0
                while j<n and i<len(s):
                    #print(i,j,l)
                    l[j]+=s[i]
                    i+=1
                    j+=1
                if i==len(s):
                    break
                tag=0
            else:
                j=n-2
                while j>0 and i<len(s):
                    #print(i,j,l)
                    l[j]+=s[i]
                    i+=1
                    j-=1
                if i==len(s):
                    break
                tag=1
        return ''.join(l)
