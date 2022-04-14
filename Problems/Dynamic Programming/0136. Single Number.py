class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i=0
        lsn=list(set(nums))
        while i<len(lsn):
            if nums.count(lsn[i])==1:
                return lsn[i]
            i+=1
