// https://leetcode.com/problems/implement-strstr/

// Implement strStr().
// Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
// Update (2014-11-02):
// The signature of the function had been updated to return the index instead of the pointer. If you still see your function signature returns a char * or String, please click the reload button  to reset your code definition.

public class Solution {
    public int strStr(String haystack, String needle) {
        if (haystack.length() == 0 && needle.length() == 0){
            return 0;
        }
        if (needle.length() == 0){
            return 0;
        }
        int needle_len = needle.length();
        int haystack_len = haystack.length();
        if (needle_len > haystack_len){
            return -1;
        }
        for (int i = 0; i < haystack_len - needle_len + 1; i++){
            // Java use str.equals(str) to see if two strings are equal.
            if (haystack.substring(i, i+needle_len).equals(needle)){
                return i;
            }
        }
        return -1;
    }
}