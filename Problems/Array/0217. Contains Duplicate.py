class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l=list(set(nums))
        if len(nums)==len(l):
            return 0
        else:
            return 1
