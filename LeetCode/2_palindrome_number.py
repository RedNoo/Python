class Solution:
    def isPalindrome(self, x):
        result = True

        if x < 0:
            return False

        arrList = []

        counter = 0

        while x != 0:
            arrList.insert(counter, int(x % 10))
            x = int(x / 10)
            counter += 1

        d = len(arrList) % 2 == 0

        for i in range(len(arrList)):
            if arrList[i] != arrList[len(arrList) - (i + 1)]:
                result = False

        return result


s = Solution()
print(s.isPalindrome(10))