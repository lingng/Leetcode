// https://leetcode.com/problems/longest-common-prefix/

// Write a function to find the longest common prefix string amongst an array of strings.

public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0){
            return "";
        }
        int shortest_idx = 0;
        int shortest_len = Integer.MAX_VALUE;
        for (int i = 0; i < strs.length; i++){
            if (strs[i].length() < shortest_len){
                shortest_len = strs[i].length();
                shortest_idx = i;
            }
        }
        String prefix = "";
        for (int i = 0; i < shortest_len; i++){
            String s = strs[shortest_idx];
            char c = s.charAt(i);
            boolean flag = true;
            for (int j = 0; j < strs.length; j++){
                if (strs[j].charAt(i) != c){
                    flag = false;
                    break;
                }
            }
            if (flag){
                prefix = prefix + c;
            }
            else{
                break;
            }
        }
        return prefix;
    }
}
