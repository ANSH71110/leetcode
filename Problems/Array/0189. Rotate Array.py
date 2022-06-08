class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if k%n!=0:
            k%=n
            i=n
            while i>n-k:
            #print(i,l)
                nums.insert(0,nums.pop(-1))                
                i-=1
