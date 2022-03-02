class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i=0
        index=0
        ve=0
        try:
            while i<len(s):   
                if t.index(s[i])>=0:
                    t=t[t.index(s[i])+1::]
                i+=1
        except ValueError:
            ve=1
            return 0                              
        if ve==0:
            return 1                   
