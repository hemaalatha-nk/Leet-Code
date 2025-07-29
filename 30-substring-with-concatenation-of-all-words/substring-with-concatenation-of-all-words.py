class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        l_w=len(words[0])
        l, r=0,l_w*len(words)
        ans=[]

        while l<len(s) and r<=len(s):
            temp=[]
            tempw=s[l:r]

            for t in range(0,len(tempw),l_w):
                temp.append(tempw[t:t+l_w])
            if sorted(temp)== sorted(words):
                ans.append(l)
            l+=1
            r+=1
        return ans





    

    

