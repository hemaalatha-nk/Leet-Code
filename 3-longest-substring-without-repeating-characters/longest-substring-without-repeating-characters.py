class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==0):
            return 0
        if(len(s)==1):
            return 1
        t=s[0]
        sub_str=[]
        list_str=[]
        long_str=0
        for i in range(1,len(s)):
            print(i,s[i],t)
            if s[i] in t:
                if(len(t)>0):
                    sub_str.append(t)
                    if(len(t)>long_str):
                        long_str=len(t)
                t=t.split(s[i])[1]
                t= t+s[i]
            else:
                t= t+s[i]
        if(len(t)>long_str):
            long_str=len(t) 
        return long_str
                
        
