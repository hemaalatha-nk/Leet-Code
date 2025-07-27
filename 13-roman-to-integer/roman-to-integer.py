class Solution:
    def romanToInt(self, s: str) -> int:

        s=list(s)
        h_table={'I':1, 'V': 5, 'X':10, 'L':50,'C':100,'D':500,'M':1000}
        res=h_table[s[0]]
        prev=h_table[s[0]]
        i=1

        while i < len(s):
            print(h_table[s[i]], prev)
            if(prev>=h_table[s[i]]):
                res+=h_table[s[i]]
                
            else:
                res=res-(2*prev) + h_table[s[i]]
            prev=h_table[s[i]]
            i+=1


        # for i in range(len(s)-2, -1, -1):
        #     if s[i] in h_table:
        #         print(h_table[s[i]], prev)
        #         if(prev > h_table[s[i]]):
        #             res+= prev - h_table[s[i]] 
        #         else:
        #             res+=h_table[s[i]]
        #         print(res)
        #         prev= h_table[s[i]]
        #     else:
        #         return 0
        
        return res


        
        