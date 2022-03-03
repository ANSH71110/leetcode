class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        ar=[]
        d=[]
        b=[]
        count=1
        if n>=3:
            i=1
            d.append(nums[1]-nums[0])
            while i<n-1:
                d.append(nums[i+1]-nums[i])
                i+=1
            i=0
            while i<len(d)-1:
                if d[i+1]==d[i]:
                    count+=1
                else:
                    if count>=2:
                        ar.append(count)
                    count=1
                    dp=(nums[i+1]-nums[i])
                i+=1
            if count>=2:
                ar.append(count)
            sum=0
            i=0
            while i<len(ar):
                sum+=((ar[i])*(ar[i]-1)//2)
                i+=1
            return sum
        else:
            return 0
