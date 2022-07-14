class Solution:
    def restoreString(self, s: str, ind: List[int]) -> str:
        i=0
        ans=''
        while i<len(ind):
            ans+=s[ind.index(i)]
            i+=1
        return ans
