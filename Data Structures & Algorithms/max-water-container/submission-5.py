class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = 0
        while right > left:
            width = right - left
            height = min(heights[left], heights[right])
            area = max(area, width * height)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return area