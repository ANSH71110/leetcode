class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        l=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        i=0
        st=set()
        while i<len(words):
            s=''
            for x in words[i]:
                s+=l[ord(x)-97]
            st.add(s)
            i+=1
        return len(st)
