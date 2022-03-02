class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i=0
        ans=[]
        j=0
        while j<2:
            while i<len(nums):  
                ans.append(nums[i])
                i+=1
            if i==len(nums):
                j+=1
                i=0
        return ans
