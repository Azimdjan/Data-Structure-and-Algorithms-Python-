class Solution:
    def twoSum(self, nums, target: int):
        myList = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if (target == nums[i] + nums[j]) and (i != j):
                    myList.append(i)
                    myList.append(j)
        return myList

if __name__ == '__main__':
    myList = [1,3,23,54,234,543,2,2]
    new = Solution()
    print(new.twoSum(myList,288))