class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        low=0
        high=0
        result=0

        for i in range(1,len(prices)):
            if(prices[i]> prices[i-1]):
                result+=prices[i]-prices[i-1] 

            # if(prices[i]< prices[i-1]):
            #         high=i-1
            #         # low=i
            #         result=prices[high]-prices[low] +result

            #         print(high, low, result)
            #         low=i

            # elif(prices[low]>prices[i]):
            #     low=i

            # if(i+1==len(prices) and prices[low]<prices[i]):
            #         result=prices[i]-prices[low] +result
            #         print("case last, i", i)
        
        # while high < len(prices):
        #     if(prices[low] > prices[high]):
        #         low=high
        #         result= max() prices[]
            # else:
                # high
            # high+=1


        return result

        