class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=0
        y=len(nums)-1
        while x<y:
            if nums[x]+nums[y]==target:
                return [x+1,y+1]
            elif nums[x]+nums[y]>target:
                y-=1
            else:
                x+=1
