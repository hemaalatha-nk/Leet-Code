class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []
        else:
            digitMap = { 
                "2" : "abc",
                "3" : "def",
                "4" : "ghi",
                "5" : "jkl",
                "6" : "mno",
                "7" : "pqrs",
                "8" : "tuv",
                "9" : "wxyz"
            }
            res = []
            def phoneNumber(indx : int, currComb : list[str]):
                if len(currComb) == len(digits):
                    res.append("".join(currComb))
                    return
                for c in digitMap[digits[indx]]:
                    currComb.append(c)
                    phoneNumber(indx + 1, currComb)
                    currComb.pop()
            phoneNumber(0, [])
            return res

        # if not digits:
        #     return []
        
        # digit_to_chars = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        # combinations=[""]

        # for digit in digits:

        #     letters=digit_to_chars[int(digit)]

        #     combinations=[prefix + letter for prefix in combinations for letter in letters]
        #     print(combinations)

        # return combinations

        