class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minC = [float('inf')] * (amount + 1)
        minC[0] = 0

        for coin in coins:
            for amount in range(1, amount + 1):
                if coin <= amount:
                    minC[amount] = min(
                        minC[amount],
                        1 + minC[amount - coin])

        if minC[amount] == float('inf'):
            return -1
        else:
            return minC[amount]