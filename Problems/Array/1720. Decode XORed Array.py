class Solution:
    def decode(self, e: List[int], first: int) -> List[int]:
        ans=[]
        ans.append(first)
        i=0
        while i<len(e):
            ans.append(ans[i]^e[i])
            i+=1
        return ans
