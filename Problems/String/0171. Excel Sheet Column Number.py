import math
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n=len(columnTitle)
        i=0
        sum=0
        while i<n:
            sum+=(ord(columnTitle[i])-64)*(math.pow(26,n-i-1))
            i+=1
        return int(sum)
