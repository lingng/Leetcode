// https://leetcode.com/problems/find-the-duplicate-number/

// Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
// Note:
// You must not modify the array (assume the array is read only).
// You must use only constant, O(1) extra space.
// Your runtime complexity should be less than O(n2).
// There is only one duplicate number in the array, but it could be repeated more than once.


public class Solution {
    public int findDuplicate(int[] nums) {
        for (int i = 0; i < nums.length; i++){
            if (nums[i] == i+1){
                continue;
            }
            else{
                while (nums[i] != i+1){
                    if (nums[nums[i]-1] != nums[i]){
                        int tmp = nums[nums[i]-1];
                        nums[nums[i]-1] = nums[i];
                        nums[i] = tmp;
                    }
                    else{
                        return nums[i];
                    }
                }
            }
        }
        return 0;
    }
}