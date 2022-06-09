class Solution:
    def reverseVowels(self, s: str) -> str:
        x=0
        y=len(s)-1
        st=('a','e','i','o','u','A','E','I','O','U')
        l=list(s)
        while x<y:
            if l[x] in st and l[y] in st:
                l[x],l[y]=l[y],l[x]
                x+=1
                y-=1
            
            if l[x] not in st:
                x+=1
            if l[y] not in st:
                y-=1
        return ''.join(l)
