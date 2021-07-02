class Solution:
    def reverse(self, x: int) -> int:
        stringRep = str(x)
        reversedString = stringRep[::-1]
        if(reversedString[len(reversedString)-1]=='-'):
            reversedString = reversedString[:len(reversedString)-1]
            actualNumber = int(reversedString)*-1
        else:
            actualNumber = int(reversedString)
        if actualNumber > 2**31 or actualNumber< -2**31:
            return 0
        return actualNumber

if __name__ == '__main__':
    num = Solution()
    print(num.reverse(2**31))