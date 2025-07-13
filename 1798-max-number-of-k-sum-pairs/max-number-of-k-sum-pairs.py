from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        operations = 0
        
        for num in list(count.keys()):
            complement = k - num
            if complement in count:
                if complement == num:
                    # Case where both numbers are same: e.g., [3,3,3] with k = 6
                    operations += count[num] // 2
                else:
                    # Pair num and its complement, like (2,3) when k=5
                    pairs = min(count[num], count[complement])
                    operations += pairs
                    count[num] = 0
                    count[complement] = 0
        
        return operations
