class Solution:
    def romanToInt(self, s: str) -> int:

        # s=list(s)
        h_table={'I':1, 'V': 5, 'X':10, 'L':50,'C':100,'D':500,'M':1000}
        prev, res=h_table[s[0]], h_table[s[0]]
        i=1

        while i < len(s):
            if(prev>=h_table[s[i]]):
                res+=h_table[s[i]]               
            else:
                res=res-(2*prev) + h_table[s[i]]
            prev=h_table[s[i]]
            i+=1

        
        return res


        
        