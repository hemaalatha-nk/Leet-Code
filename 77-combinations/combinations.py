class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def combinations(indx, combList):
            if indx > n + 1:
                return
            
            if len(combList) == k:
                res.append(combList[:])
                return
            for i in range(indx, n + 1):
                combList.append(i)
                combinations(i + 1, combList)
                combList.pop()
        combinations(1, [])
        return (res)