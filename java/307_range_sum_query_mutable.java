// https://leetcode.com/problems/range-sum-query-mutable/
// Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
//
// The update(i, val) function modifies nums by updating the element at index i to val.
// Example:
// Given nums = [1, 3, 5]
//
// sumRange(0, 2) -> 9
// update(1, 2)
// sumRange(0, 2) -> 8
// Note:
// The array is only modifiable by the update function.
// You may assume the number of calls to update and sumRange function is distributed evenly.

public class NumArray {
    private int[] num;
    private int len;
    private int sw;

    public NumArray(int[] nums) {
        len = nums.length;
        num = nums;
        for (int i = 0; i < len; i++){
            sw = sw+nums[i];
        }
    }

    void update(int i, int val) {
        int tmp = num[i];
        num[i] = val;
        sw = sw-tmp+val;
    }

    public int sumRange(int i, int j) {
        int s = 0;
        if (j-i+1 > len/2){
            s = sw;
            for (int k = 0; k < i; k++){
                s = s-num[k];
            }
            for (int k = j+1; k<len;k++){
                s = s-num[k];
            }
        }else{
            for (int k = i; k <= j; k++){
                s = s+num[k];
            }
        }
        return s;
    }
}


// Your NumArray object will be instantiated and called as such:
// NumArray numArray = new NumArray(nums);
// numArray.sumRange(0, 1);
// numArray.update(1, 10);
// numArray.sumRange(1, 2);
