class Solution:
    def hammingWeight(self, n: int) -> int:
        n=''.join(bin(n))
        return n.count('1')
