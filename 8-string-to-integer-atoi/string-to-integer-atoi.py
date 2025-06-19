
class Solution:
    import re
    def myAtoi(self, s: str) -> int:
        min_x=-2 ** 31
        max_x= (2 ** 31) -1
        s=s.strip() # remove white spaces
        match = re.match(r'[+-]?\d+', s)
        if(match):
            res=int(match.group())
            if(res < min_x ): return min_x
            if(res > max_x): return max_x
            return res
        else:
            return 0
                