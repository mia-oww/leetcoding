# Last updated: 7/24/2025, 1:24:18 AM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area= 0

        while left < right:
            width = right - left 
            current_area = min(height[left], height[right]) # grab MIN, the max height would overflow. 
            area = width * current_area # then get area

            max_area = max(max_area, area) # largest area so far

            if height[left]< height[right]:
                left += 1
            else:
                right -= 1
        return max_area

        