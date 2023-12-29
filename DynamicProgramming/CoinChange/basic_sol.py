class Solution:
    def coinChange(self, coins, amount) -> int:
        MAXI = float('inf')
        res = [0] + [MAXI] * amount
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    res[i] = min(res[i], res[i - coin] +1)
        return res[amount] if res[amount] != float('inf') else -1 

    
if __name__ == "__main__":
    sol = Solution()
    sol = sol.coinChange([1,2,5], 11)
    print(sol)

    