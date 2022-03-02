class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rs=[]
        rs.append(nums[0])
        i=1
        while i<len(nums):
            rs.append(rs[i-1]+nums[i])
            i+=1
        return rs
