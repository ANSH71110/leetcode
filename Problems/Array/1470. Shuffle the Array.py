class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        a=nums[0:n]
        b=nums[n:]
        i=0
        c=[]
        while i<n:
            c.append(a[i])
            c.append(b[i])
            i+=1
        return c
