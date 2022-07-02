class Solution:
    def maximumUnits(self, bt: List[List[int]], ts: int) -> int:
        bt=sorted(bt,key=lambda x :x[1],reverse=True)
        #print(bt)
        i=0
        sum=0
        while i<len(bt) and ts>0:            
            if ts>=bt[i][0]:
                ts-=bt[i][0]
                sum+=bt[i][0]*bt[i][1]
            else:
                sum+=ts*bt[i][1]
                ts=0
            i+=1
            #print(i,ts,sum)
        return sum
