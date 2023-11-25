class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1,
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000,
                 }

        checkLetter = ""
        val = []
        total = 0

        for i in s:

            if i == "I":
                if checkLetter == "":
                    checkLetter = i
                elif checkLetter == i:
                    val.append(roman[checkLetter])
                    checkLetter = i
            elif i == "V":
                 pass

        total = sum(val)

        return total


s = Solution()
print(s.romanToInt("VI"))
