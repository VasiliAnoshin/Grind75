### [Simple Solution](/Array/TrappingRainWater/basic_sol.py): Extra space

```python
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft, maxRight = [0] * n, [0] * n
        
        for i in range(1, n):
            maxLeft[i] = max(height[i-1], maxLeft[i-1])
        for i in range(n-2, -1, -1):
            maxRight[i] = max(height[i+1], maxRight[i+1])
            
        ans = 0
        for i in range(n):
            waterLevel = min(maxLeft[i], maxRight[i])
            if waterLevel >= height[i]:
                ans += waterLevel - height[i]
        return ans
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), 
Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

Solution 1: Max Left, Max Right So Far!
- A ith bar can trap the water if and only if there exists a higher bar to the left and a higher bar to the right of ith bar.
- To calculate how much amount of water the ith bar can trap, we need to look at the maximum height of the left bar and the maximum height of the right bar, then
    - The water level can be formed at ith bar is: waterLevel = min(maxLeft[i], maxRight[i])
    - If waterLevel >= height[i] then ith bar can trap waterLevel - height[i] amount of water.
-To achieve in O(1) when looking at the maximum height of the bar on the left side and on the right side of ith bar, we pre-compute it:
    - Let maxLeft[i] is the maximum height of the bar on the left side of ith bar.
    - Let maxRight[i] is the maximum height of the bar on the right side of ith bar.