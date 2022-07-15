class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        i=0
        while i<len(nums):
            #print(nums)
            if index[i]!=i:
                nums.insert(index[i],nums.pop(i))
            i+=1
        return nums
