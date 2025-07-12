import re
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=set("aAIiEeOoUu")
        s=list(s)

        left, right= 0, len(s)-1

        while left< right:
            if(s[left] not in vowels):
                left=left+1
            elif(s[right] not in vowels):
                right=right-1
            else:
                s[left], s[right]= s[right], s[left]
                left+=1
                right-=1
        s="".join(s)
        return s



        # l=re.findall("[aAIiEeOoUu]",s)
        # for i in range(len(s)-1,-1,-1):
        #     if s[i] in ["a","A","I","i","E","e","O","o",'U',"u"]:
        #         s=s[:i]+ l[0]+s[i+1:]
        #         l.pop(0)
        # return s

        