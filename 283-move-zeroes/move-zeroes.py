class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right_pointer=1
        count=0
        left_pointer=0
        print(len(nums))
        if(1 > len(nums) or len(nums) > math.pow(10,4)):
            return
        while right_pointer <len(nums):
            if(nums[left_pointer]==0):
                    nums[right_pointer], nums[left_pointer]=nums[left_pointer], nums[right_pointer]
                    if(nums[left_pointer]!=0):
                        left_pointer+=1
                    right_pointer+=1
            else: 
                # i+=1
                left_pointer+=1
                right_pointer+=1
            #     count+=1
            #     print("0: ",i, nums[i])
            #     for j in range(i,(len(nums)-1)):
            #             nums[j]=nums[j+1]
            #             print("shift ",j,nums[j], nums[j+1])
            #     nums[-1]=0
            #     i-=1
            #     # if(i==0):
            #     #     i-=1
            # else:
            #     i-=1
            #     print("not 0:", i)
            
                    
            

                

        