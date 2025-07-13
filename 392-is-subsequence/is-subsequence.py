class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s=list(s)
        t=list(t)

        s_p=0
        t_p=0
        _re=False
        if(len(s)==0):
            return True

        while s_p<len(s) and t_p<len(t):
            print(s_p,t_p)
            if(s[s_p]==t[t_p]):
                _re=True
                s_p+=1
                t_p+=1
            else:
                _re=False
                t_p+=1
        if(s_p>=len(s)):
            return True
        else:
            return False




            