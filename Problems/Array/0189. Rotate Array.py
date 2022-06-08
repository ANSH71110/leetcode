class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=[]
        n=len(nums)
        if k%n!=0:
            k%=n
            i=n-k
            while i<n:
            #print(i,l)
                l.append(nums[i])
                i+=1
            i=0
            while i<=n-k:
            #print(i,l)
                l.append(nums[i])
                i+=1
            i=0
            while i<n:
                nums[i]=l[i]
                i+=1
