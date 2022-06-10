class Solution:
    def numJewelsInStones(self, j: str, s: str) -> int:
        i=0
        count=0
        while i<len(j):
            c=j[i]
            k=0
            while k<len(s):
                if c==s[k]:
                    count+=1
                k+=1
            i+=1
        return count
