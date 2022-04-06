class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        area=0
        while i<j:
            area=max(area,(j-i)*min(height[j],height[i]))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return area
                    
