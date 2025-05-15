// Last updated: 5/15/2025, 3:45:56 PM
// solved using hashmap
class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> roman = new HashMap<>();
        roman.put('I', 1);
        roman.put('V', 5);
        roman.put('X', 10);
        roman.put('L', 50);
        roman.put('C', 100);
        roman.put('D', 500);
        roman.put('M', 1000);

        int result = 0;
        for(int i = 0; i <s.length(); i++){
            int current = roman.get(s.charAt(i));
            if(i < s.length() - 1 && current < roman.get(s.charAt(i+1))){
                result -= current;
            } else{
                result += current;
            }
            }
            return result;
        }
    }
