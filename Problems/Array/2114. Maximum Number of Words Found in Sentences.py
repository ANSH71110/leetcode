class Solution(object):
    def mostWordsFound(self, s):
        """
        :type sentences: List[str]
        :rtype: int
        """
        i=0
        m=0
        while i<len(s):
            g=[]
            g=list(s[i].split(" "))
            if m<len(g):
                m=len(g)
            i+=1
        return m
