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