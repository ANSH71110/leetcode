class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        i=0
        nums.sort()
        lion=[]
        while i<len(nums)-3:
            #print(nums,lion)
            j=i+1
            while j<len(nums)-2:
                k=j+1
                l=len(nums)-1
                while k<l:
#                    print(i,j,k,l)
                    sum=nums[i]+nums[j]+nums[k]+nums[l]
                    if sum==target:
                        t=[nums[i],nums[j],nums[k],nums[l]]
                        if t not in lion:
                            lion.append(t)
                        k+=1
                        while nums[k]==nums[k-1] and k<l:
                            k+=1
                    elif sum<target:
                        k+=1
                        while nums[k]==nums[k-1] and k<l:
                            k+=1
                    else:
                        l-=1
                        while nums[l]==nums[l+1] and l>k:
                            l-=1
                j+=1
            i+=1
        return lion
