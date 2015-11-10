// https://leetcode.com/problems/longest-palindromic-substring/

// Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

public class Solution {
    public String longestPalindrome(String s) {
        boolean[][] P = new boolean[s.length()][s.length()];
        int max = 0;
        int start = 0;
        for (int k = 0; k < s.length(); k++) {
            for (int i = 0; i < s.length() - k; i++) {
                if (s.charAt(i) == s.charAt(i + k)) {
                    if (k < 2 || P[i + 1][i + k - 1]) {
                        P[i][i + k] = true;
                        if (k > max) {
                            max = k;
                            start = i;
                        }
                    }
                }
            }
        }
        return s.substring(start, start + max + 1);
    }
}