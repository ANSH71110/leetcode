class Solution(object):
    def finalValueAfterOperations(self, o):
        """
        :type operations: List[str]
        :rtype: int
        """
        a=0
        i=0
        while i<len(o):
            if "+" in o[i]:  
                a+=1
            else:
                a-=1
            i+=1
        return a
