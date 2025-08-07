from collections import defaultdict
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        mark = defaultdict(int)
        subList = []
        res = []
        def permutation(mark, subList):
            if len(subList) == len(nums):
                res.append(subList[:])
                return
            for i in range(len(nums)):
                # print("First", nums[i], mark)
                if mark[nums[i]] != 1:
                    subList.append(nums[i])
                    mark[nums[i]] = 1
                    permutation(mark, subList)
                    subList.pop()
                    mark[nums[i]] = 0
        permutation(mark, subList)

        return res





        # def backtrack():
        #     if len(p) == n:
        #         res.append(p[:])
        #         return

        #     for x in nums:
        #         if x not in p:
        #             p.append(x)
        #             # print(p)
        #             backtrack()
        #             p.pop()

        # backtrack()
        # return res



        