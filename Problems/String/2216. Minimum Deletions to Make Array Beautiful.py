class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        i,s=0,0
        while i<len(nums)-1:
            if (i-s)%2==0 and nums[i]==nums[i+1]:
                s+=1
            i+=1
        return s+(len(nums)-s) %2
