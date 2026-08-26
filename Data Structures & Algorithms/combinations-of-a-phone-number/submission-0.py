class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar =  {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def backtrack(index, curString):
            if len(curString) == len(digits):
                return res.append(curString)

            for char in digitToChar[digits[index]]:
                backtrack(index + 1, curString + char)

        if len(digits) >= 1: 
            backtrack(0, "")
        return res    

        