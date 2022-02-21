class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        n=len(nums)//2 
        s=set(nums)
        for item in s:
            if nums.count(item)>n:
                return item
