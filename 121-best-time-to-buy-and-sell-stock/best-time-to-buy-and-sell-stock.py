class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min = max=0
        result=0

        for i in range(1, len(prices)):
            if (prices[i]< prices[min]):
                print(i)
                min=i
                if(max < min):
                    max=min
            elif(prices[i]>prices[max]):
                print(i)
                max=i
                if(min<max):
                    if(result< prices[max]- prices[min] ):
                        result= prices[max]- prices[min]

        return result




        