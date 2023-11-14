### [Simple Solution](/Array/BestTimeToBuyStocks/basic_sol.py): Greedy solution

```python
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        global_min = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            global_min = min(global_min, prices[i])
            profit = max(profit, prices[i]-global_min)
        return profit
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
Explanation: The idea behind this algorithm is to track the minimum price encountered so far (global_min) and calculate the profit that can be obtained by selling at the current price (prices[i]) minus the minimum price. The maximum profit is updated whenever a higher profit is found during the iteration.