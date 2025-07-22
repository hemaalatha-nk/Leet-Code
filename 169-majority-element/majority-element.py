class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        majority_ele={}
        result=0
        n=len(nums)/2

        for i in range(0,len(nums)):
            if nums[i] in majority_ele:
                majority_ele[nums[i]]=  majority_ele[nums[i]]+1
            else:
                 majority_ele[nums[i]]=1
        
            if(majority_ele[nums[i]]>n):
                n=majority_ele[nums[i]]
                result=nums[i]
            # print(majority_ele[nums[i]] )
        return result


        