public class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> queue = new PriorityQueue<Integer>(k);
        for (int num : nums) {
            if (queue.size() < k) {
                queue.add(num);
            } else if (queue.peek()< num) {
                queue.remove();
                queue.add(num);
            }
        }
        return queue.peek();
    }

    public int findKthLargest_1(int[] nums, int k) {
        return findPos(nums, 0, nums.length - 1, k);
    }
    
    private int findPos(int[] nums, int start, int end, int order) {
        int pivot = nums[start];
        int smaller = start;
        int greater = end + 1;
        int index = start + 1;
        while (index < greater) {
            if (nums[index] <= pivot) {
                smaller++;
                index++;
            } else {
                int tmp = nums[--greater];
                nums[greater] = nums[index];
                nums[index] = tmp;
            }
        }
        index--;
        nums[start] = nums[index];
        nums[index] = pivot;
        if (end - index == order - 1) {
            return pivot;
        } else if (end - index < order - 1) {
            return findPos(nums, start, index - 1, order - (end - index) - 1);
        } else {
            return findPos(nums, index + 1, end, order);
        }
    }

    public int findKthLargest_2(int[] nums, int k) {
        Arrays.sort(nums);
        return nums[nums.length-k];
    }
}