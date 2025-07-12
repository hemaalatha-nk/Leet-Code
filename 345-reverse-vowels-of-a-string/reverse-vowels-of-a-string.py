import re
class Solution:
    def reverseVowels(self, s: str) -> str:
        l=re.findall("[aAIiEeOoUu]",s)
        lLen=len(l)
        
    
        for i in range(len(s)-1,-1,-1):
          
            if s[i] in ["a","A","I","i","E","e","O","o",'U',"u"]:
                s=s[:i]+ l[0]+s[i+1:]
                l.pop(0)
        return s

        