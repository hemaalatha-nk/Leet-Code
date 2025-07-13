class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                # Found third number greater than both
                return True
        return False

        # x_min=0
        # x_max=0
        # x_mid=0
        # for i in range(2,len(nums)):
        #     x_min, x_max, x_mid=0,0,0
        #     # print(nums[i-2],nums[i-1],nums[i])
        #     if(nums[i-2]<=nums[i-1]):
        #         x_min=nums[i-2]
        #         if(nums[i-1]<=nums[i]):
        #             x_mid=nums[i-1]
        #             x_max=nums[i]
        #         print(x_min , x_mid , x_max, (x_min < x_mid < x_max))
        #         if (x_min < x_mid < x_max): 
        #             return True
        # return False
        