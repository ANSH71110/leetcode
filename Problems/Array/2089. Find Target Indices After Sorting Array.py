class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l=[]
        nums.sort()
        i=0
        while i<len(nums):
            if nums[i]==target:
                l.append(i)
            elif nums[i]>target:
                return l
            i+=1
        return l
