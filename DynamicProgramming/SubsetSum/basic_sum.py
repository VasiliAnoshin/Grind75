class Solution:
    def canPartition(self, nums) -> bool:
        if sum(nums)%2!=0:
            return False
        dp = set()
        dp.add(0) # add first elm for start calculation. i.e [1.2.3.4] 0 +1. 0 +11. We need option to add elm itself to output.
        target = sum(nums)//2
        for num in nums: 
            new_dp = set() #we add new collection as we cant change collection that we are runnig on.
            for elm in dp: 
                new_dp.add(elm + num)
                new_dp.add(elm)
            dp = new_dp
        return True if target in dp else False 

if __name__ == '__main__':
    sol = Solution()
    sol.canPartition([1,5,11,5])