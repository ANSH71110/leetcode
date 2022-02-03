class Solution:
    def mySqrt(self, x: int) -> int:
        i=2
        if x==0:
            return 0
        elif x<4:
            return 1
        else:
            if x%2==0:
                hf=x//2
            else:
                hf=x//2 +1
            while i<=hf:
                if i==(x//i):
                    return i
                elif i>(x//i):
                    return i-1
                i+=1
