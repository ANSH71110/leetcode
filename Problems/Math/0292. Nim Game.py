class Solution:
    def canWinNim(self, n: int) -> bool:
        n=n%4
        if n==0:
            return 0
        else:
            return 1
