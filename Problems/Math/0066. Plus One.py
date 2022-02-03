class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=digits[::-1]
        digits[0]+=1
        i=0
        while i<len(digits):
            if digits[i]>9:
                digits[i]=0
                if i==len(digits)-1:
                    digits.append(1)
                else:
                    digits[i+1]+=1
            i+=1
        digits=digits[::-1]
        return digits
