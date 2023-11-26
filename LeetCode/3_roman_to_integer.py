class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        x1 = {"I": "V,X", "X": "L,C", "C": "D,M"}

        temp_letter = ""
        val = []

        for i in s:
            print(i)
            if i in x1:
                print("true")
                if temp_letter == "" or temp_letter == i:
                    temp_letter = i
                    val.append(roman[i])
                elif temp_letter == x1[i][0]:
                    temp_letter = i
                    val.append(roman[i])
                elif temp_letter == x1[i][2]:
                    temp_letter = i
                    val.append(roman[i])
                elif temp_letter not in x1 and i in x1:
                    temp_letter = i
                    val.append(roman[i])
                elif i == x1[temp_letter][0] or i == x1[temp_letter][2]:
                    val.append(roman[i] - 2 * roman[temp_letter])
                    temp_letter = ""
                else:
                    temp_letter = i
                    val.append(roman[i])


            else:
                if temp_letter == "":
                    temp_letter = i
                    val.append(roman[i])
                elif temp_letter in x1:
                    if i == x1[temp_letter][0] or i == x1[temp_letter][2]:
                        val.append(roman[i] - 2*roman[temp_letter])
                        temp_letter = ""
                    else:
                        temp_letter = i
                        val.append(roman[i])
                else:
                    temp_letter = i
                    val.append(roman[i])

        print(temp_letter)
        total = sum(val)

        return total


s = Solution()

print(s.romanToInt("MCMXCIV"))
