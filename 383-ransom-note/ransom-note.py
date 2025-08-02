class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mag= {}
        rag={}

        # for m in magazine:
        #     mag[m]=mag.get(m,0)+1
        # print(mag)

        for r in ransomNote:
            rag[r]=rag.get(r,0)+1


        # for r in ransomNote:
        #     if r in mag and mag[r]>0:
        #         mag[r]-=1
        # print("mag2: ",mag)

        for m in magazine:
            if m in rag and rag[m]>0:
                rag[m]-=1
        print("rag2: ",rag)

        return (all(value == 0 for value in rag.values()))

        if ransomNote in magazine:
            return True
        return False
            
        