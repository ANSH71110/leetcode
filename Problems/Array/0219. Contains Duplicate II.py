class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        dic={}
        while i<len(nums):
            if nums[i] in dic and i-dic[nums[i]]<=k:
                return 1
            dic[nums[i]]=i
            i+=1
        return 0
