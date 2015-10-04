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

    public int[] singleNumber_1(int[] nums) {
    int xor = 0;
    // get the overall xor result. The numbers that come in pairs will results in a 0.
    for(int e:nums) {
        xor ^= e;
    }
    
    // xor will be the xor result of the two single numbers.
    // Since these numbers are different, there must be a bit, that the xor result will be 1 rather than 0.
    // Use mask and mask <<= 1 to find that bit with a 1.

    int mask = 1;
    while((mask & xor) == 0)
        mask <<= 1;
    
    // Separate all numbers into two group, those are 1 on that bit, and those are 0 on that bit.
    // Since other numbers come in pairs, thus the xor result will be zero.
    // By this way, we can get the two single numbers.
    int a = 0, b = 0;
    for(int e:nums) {
        if((mask & e) == 0) {
            a ^= e;
        } else {
            b ^= e;
        }
    }
    
    return new int[]{a, b};
}
}