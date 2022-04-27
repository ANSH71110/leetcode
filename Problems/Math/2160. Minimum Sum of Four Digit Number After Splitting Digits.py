class Solution:
    def minimumSum(self, num: int) -> int:
        l=[int(x) for x in str(num)]
        l.sort()
        return 10*(l[0]+l[1])+l[2]+l[3]
