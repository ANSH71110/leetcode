class Solution:
    def numJewelsInStones(self, j: str, s: str) -> int:
        i=0
        count=0
        while i<len(j):
            count+=s.count(j[i])
            i+=1
        return count
