class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapp={}
        stack=[]
        ans=[]
        
        for i in nums2:
            while stack and i>stack[-1]:
                mapp[stack.pop()]=i
            stack.append(i)
        
        while stack:
            mapp[stack.pop()]=-1
        
        for i in nums1:
            ans.append(mapp[i])
        
        return ans
