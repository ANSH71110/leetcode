import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        are=re.compile("[^a-zA-Z0-9]")
        swn=re.sub(are,"",s)
        swn=swn.lower()
        revswn=swn[::-1]
        if revswn==swn:
            return 1
        else:
            return 0
