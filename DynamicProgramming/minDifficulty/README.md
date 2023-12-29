### [Basic Solution](/DynamicProgramming/minDifficulty/sol.py): DP
Problem: [here](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/)!


```python
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        
        cache = {}
        def dfs(i, d, cur_max):
            if i == len(jobDifficulty):
                return 0 if d ==0 else float("inf")
            if d == 0: #if d==0 and its not end of the job list. 
                return float('inf')
            if (i,d, cur_max) in cache:
                return cache[(i,d, cur_max)]
            
            cur_max = max(cur_max, jobDifficulty[i])
            res = min(
                dfs(i+1, d, cur_max), #continue the current day
                cur_max + dfs(i+1, d-1, -1) #end day and open new one
            )
            cache[(i, d, cur_max)] = res #add current combination to cache
            return res
        return dfs(0, d, -1)
```

Time Complexity: ![O(2^d)](<https://latex.codecogs.com/svg.image?\inline&space;O(2^d))>), Space Complexity: ![O(len(jobDifficulty))](<https://latex.codecogs.com/svg.image?\inline&space;O(len(jobDifficulty))>)

Explanation:
1) The only one reason to complete recursion step is the case when number of days = 0 and you stay at the end of the job list.
in any other case return float('inf').
2) looking for cur_max at each recursion step because each day has its max. 
3) Decide what is the best solution - continue the current day or split cur day and start new one. Take min between them.

