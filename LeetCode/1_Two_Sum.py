class Solution:
    def twoSum(self, nums, target):

        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):

                if j+1+i < len(nums) and nums[i] + nums[j+1+i] == target:
                    print(j)
                    result.append(i)
                    result.append(j+1+i)
                    return result


myList =[2,7,11,15]
solution = Solution()
r = solution.twoSum(myList, 9   )
print(r)
