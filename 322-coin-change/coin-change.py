class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort()
        dp_=[0]*(amount+1)

        for i in range(1,amount+1):
            minn=float('inf')

            for c in coins:

                diff= i-c
                if diff<0:
                    break
                minn= min(minn, dp_[diff]+1)

            dp_[i]=minn
        if dp_[amount]<float('inf'):
            return dp_[amount]
        else:
            return -1

      
        # coins.sort()
        # dp_ = [float('inf')] * (amount + 1)
        # dp_[0] = 0  # Base case

        # for i in range(1, amount + 1):
        #     minn = float('inf')
        #     for c in coins:
        #         diff = i - c
        #         if diff < 0:
        #             break
        #         minn = min(minn, dp_[diff] + 1)
        #     dp_[i] = minn  # ✅ store minn

        # return dp_[amount] if dp_[amount] != float('inf') else -1
