class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mag= {}
        rag={}

        for r in ransomNote:
            rag[r]=rag.get(r,0)+1

        for m in magazine:
            if m in rag and rag[m]>0:
                rag[m]-=1

        return (all(value == 0 for value in rag.values()))
