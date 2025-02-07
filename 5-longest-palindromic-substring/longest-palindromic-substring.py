class Solution:
    def checking_palin(self, sub_str):
        while sub_str!=sub_str[::-1]:
            sub_str=sub_str[1:]
        if(len(sub_str)>1):
            if (sub_str==sub_str[ : :-1]):
                return sub_str

    def longestPalindrome(self, s: str) -> str:
        if(len(s)==1):
            return s
        ans=None
        sub_str=s[0]

        for i in range(1, len(s)):
            sub_str=sub_str+s[i]
            a=self.checking_palin(sub_str)
            if(a!=None):
                if(ans==None or len(a)>=len(ans)):
                    ans=a

        if ans!=None:
                return ans
        else:
            return s[0]

        