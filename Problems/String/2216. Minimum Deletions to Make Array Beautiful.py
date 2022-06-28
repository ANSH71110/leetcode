class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        i=0
        s=0
        while i<len(nums)-1:
            if i%2==0 and nums[i]==nums[i+1]:
                nums.pop(i)
                s+=1
                i-=1
            i+=1
        if len(nums)%2!=0:
            nums.pop(-1)
            s+=1
        return s
