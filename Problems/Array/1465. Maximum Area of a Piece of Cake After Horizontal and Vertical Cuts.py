class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        hc.append(h)
        vc.append(w)
        hc.sort()
        vc.sort()
        i=1
        maxv=vc[0]
        while i<len(vc):
            maxv=max(maxv,vc[i]-vc[i-1])
            i+=1
        i=0
        maxh=hc[0]
        while i<len(hc):
            maxh=max(maxh,hc[i]-hc[i-1])
            i+=1
        return maxv*maxh % (10**9 +7)
