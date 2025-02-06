class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if(len(s)==0 or len(s)==1):
        #     return len(s)
        t=set()
        max_len=0
        current_index=0
        for i in range(len(s)):
            while s[i] in t:
                # t.remove(s[current_index])
                t.remove(s[current_index])
                current_index+=1
            t.add(s[i])
            max_len = max(max_len, i - current_index + 1)
        return max_len
                
        
