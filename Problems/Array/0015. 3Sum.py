class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        n=len(nums)
        nums.sort()
        if n<=2:
            return l
        else:
            i=0
            while i<n:
                j=i+1
                k=n-1
                while j<k:
                    ts=nums[i]+nums[j]+nums[k]
                    if ts>0:
                        k-=1
                    elif ts<0:
                        j+=1
                    else:
                        temp=[]
                        temp.append(nums[i])
                        temp.append(nums[j])
                        temp.append(nums[k])
                        if temp not in l:
                            l.append(temp)
                        j+=1
                        while nums[j]==nums[j-1] and j<k:
                            j+=1
                i+=1
            return l
