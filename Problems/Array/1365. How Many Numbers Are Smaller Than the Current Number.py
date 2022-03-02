import copy
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=copy.copy(nums)
        n.sort()
        ls=[]
        i=0
        while i<len(nums):
            ls.append(n.index(nums[i]))
            i+=1
        return ls
