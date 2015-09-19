// https://leetcode.com/problems/move-zeroes/

// Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
// For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
// Note:
// You must do this in-place without making a copy of the array.
// Minimize the total number of operations.

// Solution from:
// http://www.geeksforgeeks.org/move-zeroes-end-array/


public class Solution {
    public void moveZeroes(int[] nums) {
        int n = nums.length;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) {
                nums[count] = nums[i];
                count = count + 1;
            }
        }
        while (count < n) {
            nums[count] = 0;
            count = count + 1;
        }
    }
}