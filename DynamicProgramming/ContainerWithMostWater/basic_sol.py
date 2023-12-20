class Solution:
    def maxArea(self, height) -> int:
        container = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                diff = j-i
                water = diff*min(height[j],height[i])
                if water > container:
                    container = water
        return container