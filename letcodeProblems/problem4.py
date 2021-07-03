class Solution:
    def romanToInt(self, s: str) -> int:
        romanConstants = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        number = 0
        previous = ''
        for i in s:
            if (i == 'X' or i=='V') and previous == 'I':
                number-=2*romanConstants[previous]
            elif (i == 'C' or i=='L') and previous == 'X':
                number-=2*romanConstants[previous]
            elif (i == 'D' or i=='M') and previous == 'C':
                number-=2*romanConstants[previous]
            number+=romanConstants[i]
            previous = i
        return number

if __name__ == '__main__':
    obj = Solution()
    print(obj.romanToInt('LVIII'))