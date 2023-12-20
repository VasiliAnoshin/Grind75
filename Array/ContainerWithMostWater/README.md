### [Basic Solution](/DynamicProgramming/ContainerWithMostWater/basic_sol.py): BruteForce

```python
    def maxArea(self, height) -> int:
        container = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                diff = j-i
                water = diff*min(height[j],height[i])
                if water > container:
                    container = water
        return container
```

Time Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>), Space Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

Explanation:
    Brute force solution. Iterate over all possible combination between (i,j).

```python
    def maxArea(self, height: List[int]) -> int:
        i,j,water =0,len(height)-1,0
        while i<=j:
            water = max(water, (j-i)*min(height[i], height[j]))
            if height[j] >= height[i]:
                i+=1
            else:
                j-=1
        return water
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n))>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
Explanation:
    I've seen some "proofs" for the common O(n) solution, but I found them very confusing and lacking. Some even didn't explain anything but just used lots of variables and equations and were like "Tada! See?". I think mine makes more sense:

Idea / Proof:
The widest container (using first and last line) is a good candidate, because of its width. Its water level is the height of the smaller one of first and last line.
All other containers are less wide and thus would need a higher water level in order to hold more water.
The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.

Further explanation:
Variables i and j define the container under consideration. We initialize them to first and last line, meaning the widest container. Variable water will keep track of the highest amount of water we managed so far. We compute j - i, the width of the current container, and min(height[i], height[j]), the water level that this container can support. Multiply them to get how much water this container can hold, and update water accordingly. Next remove the smaller one of the two lines from consideration, as justified above in "Idea / Proof". Continue until there is nothing left to consider, then return the result.


