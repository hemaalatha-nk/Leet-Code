class Solution:
    def reverseWords(self, s: str) -> str:

        s=s.strip().split()
        left, right=0, len(s)-1
        if " " in s:
            s.remove(" ")

        while left< right:
             s[left], s[right]= s[right], s[left]
             left+=1
             right-=1
        return " ".join(s)
        