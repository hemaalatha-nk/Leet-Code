class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:


        if len(nums)== len(set(nums)):
            return False
        l=0
        window=set()

        for r in range(len(nums)):
            if r-l > k:
                window.remove(nums[l])
                l+=1
            if nums[r] not in window:
                window.add(nums[r])
            else:
                return True
        return False


        