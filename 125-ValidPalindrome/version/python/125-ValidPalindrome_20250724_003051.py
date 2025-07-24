# Last updated: 7/24/2025, 12:30:51 AM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two-pointer method
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum(): # skipping non-alphanumeric
                left += 1 
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower(): # check lowercase
                return False
            left+= 1 
            right -= 1

        return True

        