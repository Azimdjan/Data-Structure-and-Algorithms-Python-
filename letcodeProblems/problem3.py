class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        reversedString = string[::-1]
        return string == reversedString

if __name__ == '__main__':
    num = Solution()
    print(num.isPalindrome(-121))