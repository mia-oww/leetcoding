// Last updated: 7/4/2025, 4:27:54 PM
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int result = 0;

        for(int i = 0; i < n; i++){
            boolean[] visited = new boolean[128];
            for(int j = i; j < n; j++){
                if(visited[s.charAt(j)] == true)
                break;
                else{
                    result = Math.max(result, j - i + 1);
                    visited[s.charAt(j)] = true;
                }
            }
        }
        return result;
    }
}