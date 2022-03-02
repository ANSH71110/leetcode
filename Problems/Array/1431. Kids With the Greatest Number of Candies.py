class Solution(object):
    def kidsWithCandies(self, c, ec):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        tf=[]
        i=0
        m=max(c)
        while i<len(c):
            if c[i]+ec<m:
                tf.append(0)
            else:
                tf.append(1)
            i+=1
        return tf
