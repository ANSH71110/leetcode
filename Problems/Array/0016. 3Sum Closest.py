class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        i=0
        l=10**10
        while i<len(nums):
            x1=i
            x2=i+1
            x3=len(nums)-1
            while x2<x3:
                sum= nums[x1]+nums[x2]+nums[x3]
                diff=sum-target
                if abs(l-target)>abs(diff):
                        l=sum
                
                if diff==0:
                    return sum
                elif diff<0:
                    x2+=1
                    while nums[x2]==nums[x2-1] and x2<x3:
                        x2+=1
                else:
                    x3-=1
                    while nums[x3]==nums[x3+1] and x3>x2:
                        x3-=1
                    
            i+=1
        return l
