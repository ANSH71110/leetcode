class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        while i<len(nums):
            if nums[i]==0:
                nums.pop(i)
                j+=1
            else:
                i+=1
        while j>0:
            nums.append(0)
            j-=1
        return nums
            
