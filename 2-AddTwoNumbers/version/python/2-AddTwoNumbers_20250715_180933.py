# Last updated: 7/15/2025, 6:09:33 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]

            if sum == target:
                return [left + 1, right + 1] # [0]->[1]
            elif sum < target:
                left += 1
            else:
                right -= 1
