class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map={}

        for i in range(len(nums)):
            diff=target-nums[i]

            # if diff<0:
            #     continue
            if nums[i] in hash_map:
                return [i, hash_map[nums[i]]]
            elif diff not in hash_map:
                hash_map[diff]=i



        