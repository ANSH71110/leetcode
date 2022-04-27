class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return 0
        if math.log10(n)/math.log10(3) %1==0:
            return 1
        else:
            return 00326. Power of Three
