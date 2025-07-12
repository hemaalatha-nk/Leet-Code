class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies= max(candies)
        resu=[]
        for c in candies:
            print(c)
            if(c+extraCandies>=maxCandies):
                 resu.append(True)
            else: resu.append(False)
        return resu
        