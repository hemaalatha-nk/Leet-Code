class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        r=0
        l=len(s)
        print(s[r:l])
        prevp=""

        while l>r:
            p=s[r:l]
            # print(p)
            # print(l,r+1)
            if p==p[::-1]:
                if len(prevp)<len(p):
                    prevp=p
                r=r+1
                l=len(s)
                    
            elif l!=r+2:
                l=l-1
            else:
                r=r+1
                l=len(s)
        return prevp
        # if len(s)==1:
        #     return s

       