class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        msum=0
        i=0
        while i<len(accounts):
            if msum<sum(accounts[i]):
                msum=sum(accounts[i])
            i+=1
        return msum
