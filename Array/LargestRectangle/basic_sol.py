class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        output = 0
        for i, h in enumerate(heights+[0]):
            while stack and heights[stack[-1]] >= h:
                H = heights[stack.pop()]
                W = i if not stack else i - stack[-1] -1
                output = max(output, H*W)
            stack.append(i)
        return output