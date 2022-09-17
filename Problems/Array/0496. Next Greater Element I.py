class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        mapp={}
        
        for i in nums2:
            while stack and i>stack[-1]:
                mapp[stack.pop()]=i
            stack.append(i)
        
        return [mapp.get(i,-1) for i in nums1]
