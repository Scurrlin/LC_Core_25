class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minC = [amount + 1] * (amount + 1)
        minC[0] = 0
        
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    minC[i] = min(minC[i], 1 + minC[i - c])
        return minC[-1] if minC[-1] != amount + 1 else -1