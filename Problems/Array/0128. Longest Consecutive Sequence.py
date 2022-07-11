class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        l=0
        lo=0
        for i in nums:
            if i-1 not in nums:
                l=1
                while i+l in nums:
                    l+=1
                lo=max(lo,l)
        return lo
