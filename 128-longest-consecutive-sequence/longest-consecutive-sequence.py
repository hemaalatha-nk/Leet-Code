class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest=0
        numset=set(nums)
        # if len(nums)==0 or len(nums)> 10 ** 5:
        #     return 0

        for n in numset:
            # lenght=0
            if (n-1) not in numset:
                next_num=n+1
                length=1
                while (next_num) in numset:
                    length+=1
                    next_num+=1
                longest=max(length,longest)
        return longest
 

       