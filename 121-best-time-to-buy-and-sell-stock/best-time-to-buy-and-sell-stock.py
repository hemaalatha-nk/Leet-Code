class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # min = max=0
        result=0

        l=0
        r=1

        while r<len(prices):
            if(prices[l]< prices[r]):
                # profit= prices[r]- prices[l]
                result=max((prices[r]- prices[l]), result)
            else:
                l=r
            r=r+1
        return result

            

        # for i in range(1, len(prices)):
        #     if (prices[i]< prices[min]):
        #         # print(i)
        #         min=i
        #         if(max < min):
        #             max=min
        #     elif(prices[i]>prices[max]):
        #         # print(i)
        #         max=i
        #         if(min<max):
        #             # if(result< prices[max]- prices[min] ):
                    
        #                 result= max((prices[max]- prices[min]), result)

        # return result




        