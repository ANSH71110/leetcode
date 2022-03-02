class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=list(s.split(" "))
        i=-1
        while len(l[i])==0:
            i-=1
        return len(l[i])
