class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        i=0
        while i<len(nums):
            ans.append(nums[nums[i]])
            i+=1
        return ans
        
