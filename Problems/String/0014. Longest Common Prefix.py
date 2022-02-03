class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i=0
        sub=""
        smin=min(strs,key=len)
        indexmin=strs.index(smin)
        if len(strs)>1:
            while i<len(strs[indexmin]):
                j=c=0
                sub+="".join(smin[i])
                while j<len(strs):   
                    if strs[j].startswith(sub) == 1: 
                        c+=1
                    j+=1
                if c!=j:
                    return sub[0:-1]
                i+=1
            return sub
        else:
            return strs[0]
