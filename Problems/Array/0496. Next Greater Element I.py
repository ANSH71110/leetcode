class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        t=[]
        for i in nums1:
            j=nums2.index(i) + 1
            if j==len(nums2) or i==max(nums2):
                t.append(-1)
            else:
                while j<len(nums2):
                    if nums2[j]>i:
                        t.append(nums2[j])
                        break
                    j+=1
                if j==len(nums2):
                    t.append(-1)
        return t
