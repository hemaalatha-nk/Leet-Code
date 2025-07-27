class Solution:
    def romanToInt(self, s: str) -> int:

     
        h_table={'I':1, 'V': 5, 'X':10, 'L':50,'C':100,'D':500,'M':1000}
        res=0

        for i in range(len(s)):
            if(i+1<len(s) and h_table[s[i+1]]>h_table[s[i]]):
                res-=h_table[s[i]]               
            else:
                res+= h_table[s[i]]

        
        return res


        
        