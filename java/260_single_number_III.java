// https://leetcode.com/problems/single-number-iii/

// Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
// For example:
// Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
// Note:
// The order of the result is not important. So in the above example, [5, 3] is also correct.
// Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

public class Solution {
    public int[] singleNumber(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++){
            if (map.containsKey(nums[i])){
                map.remove(nums[i]);
            }
            else{
                map.put(nums[i], 1);
            }
        }
        int[] result = new int[2];
        int idx = 0;
        for (Integer key: map.keySet()){
            result[idx] = key;
            idx = idx + 1;
        }
        return result;
    }
}