class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        d=0
        try:
            if nums.index(target)>=0:
                return nums.index(target)
        except ValueError:
            if target<nums[0]:
                return 0
            elif target>nums[-1]:
                return len(nums)
            else:
                num=nums
                l=nums[0]
                h=nums[-1]
                n=len(nums)//2
                while d!=1:
                    m=num[n]
                    n=len(num)//2
                    if m>target:
                        h=m
                        num=num[0:n+1]
                        if nums.index(m)-nums.index(l)==1:
                            d=1
                            return nums.index(m)
                    else:
                        l=m
                        num=num[n:]
                        if nums.index(h)-nums.index(m)==1:
                            d=1
                            return nums.index(m)+1
