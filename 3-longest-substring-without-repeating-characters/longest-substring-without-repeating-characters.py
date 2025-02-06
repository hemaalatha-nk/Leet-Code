class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==0 or len(s)==1):
            return len(s)
        t=s[0]

        long_str=0
        for i in range(1,len(s)):
            if s[i] in t:
                if(len(t)>0):
                        if(len(t)>long_str):
                            long_str=len(t)
                        t=t.split(s[i])[1]
            t= t+s[i]
        if(len(t)>long_str):
            long_str=len(t) 
        return long_str
                
        
