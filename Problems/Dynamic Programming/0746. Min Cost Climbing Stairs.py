class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a=cost[0]
        b=cost[1]
        i=2
        while i<len(cost):
            c=cost[i]+min(a,b)
            a=b
            b=c
            i+=1
        return min(a,b)
