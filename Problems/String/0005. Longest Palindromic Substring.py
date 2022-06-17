class Solution:
    def longestPalindrome(self, s: str) -> str:
        i=0
        res=''
        resl=0
        while i<len(s):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r+1-l>resl:
                    res=s[l:r+1]
                    resl=len(res)
                l-=1
                r+=1
            
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r+1-l>resl:
                    res=s[l:r+1]
                    resl=len(res)
                l-=1
                r+=1
            
            i+=1
        return res
