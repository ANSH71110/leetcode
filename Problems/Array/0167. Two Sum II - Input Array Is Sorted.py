class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        l=[]
        j=len(nums)-1
        while i<j:
            #print(nums[i],nums[j],target,i,j)
            if nums[i]+nums[j]>target:
                j-=1
            elif nums[i]+nums[j]<target:
                i+=1
            else:
                l.append(i+1)
                l.append(j+1)
                return l
        return l
