### [Simple Solution](/Array/BestTimeToBuyStocks/basic_sol.py): Greedy solution

```python
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        global_min = prices[0]
        global_max = 0
        for i in range(1, len(prices)):
            global_min = min(global_min, prices[i])
            global_max = max(global_max, prices[i]-global_min)
        return global_max
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)