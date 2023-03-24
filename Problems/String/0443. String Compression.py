class Solution:
    def compress(self, chars: List[str]) -> int:
        index=0
        i=0
        while i<len(chars):
            l=chars[i]
            count=0
            while i<len(chars) and chars[i]==l:
                count+=1
                i+=1
            chars[index]=l
            index+=1
            if count > 1:
                for z in str(count):
                    chars[index]=z
                    index+=1
            
        return index
