# Last updated: 7/24/2025, 1:25:16 AM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area= 0

        while left < right:
            width = right - left 
            current_area = min(height[left], height[right]) # grabbing MIN, max height might overflow
            area = width * current_area # getting area

            max_area = max(max_area, area) # max_area = area, only update if there is a larger max_area

            if height[left]< height[right]:
                left += 1
            else:
                right -= 1
        return max_area

        