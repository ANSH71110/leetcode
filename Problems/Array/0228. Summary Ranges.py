class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i=1
        ss=[]
        if len(nums)<1:
            return ss
        f=nums[0]
        tag=0
        while i<len(nums):
            print(i,f,nums[i])
            if tag==0:
                ss.append(str(f))
            
            if nums[i]-nums[i-1]==1:
                tag=1
                l=nums[i]
            else:
                if tag==1:
                    ss[-1]=(str(f)+'->'+str(l))
                    tag=0
                f=nums[i]                
            i+=1
        if tag==0:
            ss.append(str(f))
        if tag==1:
            ss[-1]=(str(f)+'->'+str(l))
        return ss                
