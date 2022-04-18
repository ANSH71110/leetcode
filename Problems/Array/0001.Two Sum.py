class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        l=[]
        j=len(nums)
        while i<j:
            try:
                if nums.index(target-nums[i])>=0 and nums.index(target-nums[i])!=i:
                    l.append(i)
                    l.append(nums.index(target-nums[i]))
                    return l
            except ValueError:
                err=1
            finally:
                i+=1
        return l
