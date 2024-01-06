### [Solution](/DynamicProgramming/MaximumProfitinJobScheduling/sol.py): DP
Problem: [here](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)!


```python
import bisect
class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        s = [j[0] for j in jobs]
        dp =[0] * (len(startTime) + 1)
        for j in range(len(jobs)-1, -1, -1):
            pos = bisect.bisect_left(s, jobs[j][1])
            dp[j] = max(dp[j+1], dp[pos] + jobs[j][2])
        return dp[0]
```

Time Complexity: we do n binary searches ![O(n * log n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n * log n))>), 
Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n))>)

This is really interesting problem, where you need to use two tecniques: dynamic programming and binary search. Let us start our jobs by their starts. Define by dp[k] the maximum gain we can have if we can use only use jobs starting with index k. How we can find dp[k] now and why in the first places we sorted our jobs by starts?

Imagine that we taken job with number k, what we can take next? We need to wait until this job finished, that is to look at jobs[k][1] and find the first job which start more than this number: we use binary search for this with this line temp = bisect_left(S, jobs[k][1]). Finally, our gain will be jobs[k][2] + dp[temp]. Also we have another option: dp[k+1], if we do not take job k. then we can take any jobs from k+1 without restriction.

Notice also that we start from k = n-1 and move to k = 0 in the opposite direction, because to answer dp[k] query we want to already be able to ask queries for dp[>k].