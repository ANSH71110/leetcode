class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans=[]
        i=0
        while i<len(nums):
            freq=nums[i]
            val=nums[i+1]
            j=0
            while j<freq:
                ans.append(val)
                j+=1
            i+=2
        return ans
