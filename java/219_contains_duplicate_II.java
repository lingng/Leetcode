// https://leetcode.com/problems/contains-duplicate-ii/

// Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

public class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> dict = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++){
            Integer idx = dict.get(nums[i]);
            if (idx != null && idx >= 0 && i - idx <= k){
                return true;
            }
            dict.put(nums[i], i);
        }
        return false;
    }
}