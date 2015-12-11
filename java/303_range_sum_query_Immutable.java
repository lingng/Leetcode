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

    public static void main(String[] args){
        int[] nums = {-2, 0, 3, -5, 2, -1};
        NumArray numArray = new NumArray(nums);
        System.out.println(numArray.sumRange(0, 2));
        System.out.println(numArray.sumRange(2, 5));
        System.out.println(numArray.sumRange(0, 5));
    }
}


// Your NumArray object will be instantiated and called as such:
// NumArray numArray = new NumArray(nums);
// numArray.sumRange(0, 1);
// numArray.sumRange(1, 2);
