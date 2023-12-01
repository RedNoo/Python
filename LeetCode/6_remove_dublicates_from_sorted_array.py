class Solution:
    def removeDuplicates(self, nums) -> int:
        lst = []
        tmp = ""
        _count = 0
        for i in nums:
            if tmp == "":
                lst.append(i)
                tmp = i
            elif i == tmp:
                _count += 1
            else:
                lst.append(i)
                tmp = i

        retval = len(lst)


        for i in range(len(lst)):
            nums[i] = lst[i]

        difference = len(nums) - len(lst)

        for i in range(difference):
            nums.pop()

        print(nums)
        return retval


s = Solution()
list = [ 1, 1, 1]

print(s.removeDuplicates(list))
