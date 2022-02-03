class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st=set()
        l=l1=l2=0
        tag=0
        i=j=0
        if len(s)>0:
            while i<len(s):
                st.clear()
                l1=len(st)
                j=i          
                while j<len(s):
                    st.add(s[j])
                    l2=len(st)
                    if l2<=l1:
                        break
                    l1=l2
                    j+=1
                l=max(len(st),l)
                i+=1
            return l
        else:
            return 0
