// Last updated: 5/15/2025, 3:34:09 PM
// math based solution using iteration, last digit is extracted, then added to reversed number after shifting digits by multiplying by 10. original number is reduced by dividing by 10 until it becomes 0
class Solution {
    public boolean isPalindrome(int x) {
        if(x<0) return false;

        int original = x;
        int reversed = 0;

        while(x != 0){
            int digit = x % 10; // last digit
            reversed = reversed * 10 + digit; 
            x = x / 10;
        }
        return original == reversed;
    }
}