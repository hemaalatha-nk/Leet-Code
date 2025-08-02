class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        ans=[]
        start=0
        end=0
        if len(nums)==1:
            return [str(nums[0])]

        for i in range(0,len(nums)-1):
            # print(nums[i]+1,nums[i+1],start,i)
            if(nums[i]+1!=nums[i+1]):
                if(start==i):
                    ans.append(f'{nums[start]}')
                else:
                    ans.append(f"{nums[start]}->{nums[i]}")
                start=i+1
                if(start==len(nums)-1):
                    ans.append(f'{nums[start]}')
            else:
                # print("lol",i,len(nums)-2 , start)
                if(i==len(nums)-2 ):
                    ans.append(f"{nums[start]}->{nums[i+1]}")

                
        return(ans)


        