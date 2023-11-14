class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in seen: 
                return [i, seen[val]]
            else:
                seen[nums[i]] = i