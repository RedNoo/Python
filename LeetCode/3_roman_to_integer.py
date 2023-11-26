class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        x1 = {"I": "V,X", "X": "L,C", "C": "D,M"}

        tempTotal = ""
        val = []
        total = 0

        for i in s:
            if i in x1:
                print("true")
                print(i)
            else:
                print("false")
                print(i)

        total = sum(val)

        return total


s = Solution()
print(s.romanToInt("IV"))
