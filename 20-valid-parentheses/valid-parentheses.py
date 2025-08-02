class Solution:
    def isValid(self, s: str) -> bool:

        if(len(s)<=1):
            return False
        stack=[]
        stack.append(s[0])
        openB=('(','[','{')
        closeB={']':'[',')':'(','}':'{'}
        

        for b in range(1,len(s)):
            if s[b] in openB or len(stack)==0:
                stack.append(s[b])
            else :
                print(closeB[s[b]], stack[-1])
                if closeB[s[b]]==stack[-1]:
                    stack.pop()
                else:
                    return False
        return  True if len(stack)==0  else False

            

        