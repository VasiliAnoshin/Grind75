class Solution:
    def maxArea(self, height) -> int:
        i,j,water =0,len(height)-1,0
        while i<=j:
            water = max(water, (j-i)*min(height[i], height[j]))
            if height[j] >= height[i]:
                i+=1
            else:
                j-=1
        return water