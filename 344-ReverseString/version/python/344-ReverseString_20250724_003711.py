# Last updated: 7/24/2025, 12:37:11 AM
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) -1

        while left < right:
            s[left], s[right] = s[right], s[left] # flip left, right -> right, left
            left+= 1
            right -= 1
        