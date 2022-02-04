class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)        
        i=0
        if n>0:
            pf=pl=-1
            while i<n:
                if nums[i]==target:
                    if pf==-1 and pl==-1:
                        pl=pf=i
                    else:
                        if i<pf:
                            pf=i
                        elif pl<i:
                            pl=i
                i+=1
            return [pf,pl]
        else:
            return [-1,-1]
