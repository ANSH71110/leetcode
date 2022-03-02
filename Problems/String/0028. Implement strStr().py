class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle):
            if needle in haystack:
                return haystack.find(needle)
            else:
                return -1
        else:
            return 0
