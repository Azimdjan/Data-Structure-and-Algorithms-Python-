class Solution:
    def longestCommonPrefix(self, strs) -> str:
        commonPref = ''
        previous = strs[0]
        previousCommon = float('inf')
        for i in strs[1:]:
            index = 0
            common = 0
            for j in previous:
                if index == len(i) or i[index] != j:
                    break
                common+=1
                index+=1
            if previousCommon > common:
                previousCommon = common 
        commonPref = previous[:previousCommon]
        return commonPref


if __name__ == '__main__':
    obj = Solution()
    print(obj.longestCommonPrefix(['he','flow','flight']))