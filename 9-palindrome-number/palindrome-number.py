class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):  # Negative numbers and numbers ending in 0 (except 0) are not palindromes
            return False
        return str(x) == str(x)[::-1]
        # str_x=str(x)
        # t_len=len(str_x)
        # for i in range(0,t_len):
        #     if(str_x[i]!=str_x[t_len-i-1]):
        #         return False
        # return True

        

        