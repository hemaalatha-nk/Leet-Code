class Solution:
    def isPalindrome(self, x: int) -> bool:
        s_x=str(x)
        if x < 0 or (x % 10 == 0 and x != 0):  # Negative numbers and numbers ending in 0 (except 0) are not palindromes
            return False
        return s_x == s_x[::-1]

        

        