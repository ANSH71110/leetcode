import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:        
        if n<=0:
            return 0
        if math.log2(n)%1==0:
            return 1
        else:
            return 0
