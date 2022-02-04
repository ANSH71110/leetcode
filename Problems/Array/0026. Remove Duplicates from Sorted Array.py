class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        t=set(nums)
        nums.clear()
        for i in t:
            nums.append(i)
        nums.sort()
        return len(t)
