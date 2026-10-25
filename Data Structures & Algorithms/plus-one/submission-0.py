class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=len(digits)-1
        resto=1
        while i>=0:
            num=digits[i]+resto
            if num>9:
                resto= num-9
                num=resto-1
            else:
                resto=0
            print(num)
            digits[i]=num
            i-=1
        if resto!=0:
            digits.insert(0,resto)
        return digits
