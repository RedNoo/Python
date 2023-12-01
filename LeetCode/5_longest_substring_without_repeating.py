class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        lst = []
        temp_List = ""

        letter_count = len(s)

        if letter_count == 1:
            return 1
        counter = 0
        while letter_count > 0:
            counter += 1
            for i in s:
                if not i in temp_List:
                    temp_List += i
                else:
                    l = list(temp_List)

                    if len(lst) > 0:
                        if len(lst[0]) < len(l):
                            lst.clear()
                            lst.append(l)
                    else:
                        lst.clear()
                        lst.append(l)

                    temp_List = ""
                    temp_List += i

            l = list(temp_List)
            if len(lst) > 0:
                if len(lst[0]) <= len(l):
                    lst.clear()
                    lst.append(list(temp_List))
            else:
                lst.append(list(temp_List))
            temp_List = ""
            s = s[1:]
            letter_count = len(s)

            if (counter >= 255): #lucy number ascii list count
                break

        count = 0

        for item in lst:
            if len(item) > count:
                count = len(item)
                break

        return count

s = Solution()

print(s.lengthOfLongestSubstring(
    "asjrgapa"))
