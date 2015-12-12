// https://leetcode.com/problems/find-median-from-data-stream/
// Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
//
// Examples:
// [2,3,4] , the median is 3
// [2,3], the median is (2 + 3) / 2 = 2.5
//
// Design a data structure that supports the following two operations:
// void addNum(int num) - Add a integer number from the data stream to the data structure.
// double findMedian() - Return the median of all elements so far.
//
// For example:
// add(1)
// add(2)
// findMedian() -> 1.5
// add(3)
// findMedian() -> 2

class MedianFinder {

    public PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>();
    public PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>(Collections.reverseOrder());

    // Adds a number into the data structure.
    public void addNum(int num) {
        if (minHeap.size() == 0){
            minHeap.offer(num);
            return;
        }
        if (maxHeap.size() == 0){
            if (num < minHeap.peek()) {
                maxHeap.offer(num);
            } else {
                maxHeap.offer(minHeap.poll());
                minHeap.offer(num);
            }
            return;
        }
        if (num > maxHeap.peek()) {
            minHeap.offer(num);
        } else {
            maxHeap.offer(num);
        }
        if (Math.abs(maxHeap.size() - minHeap.size()) > 1) {
            balanceHeap(maxHeap, minHeap);
        }

    }

    public void balanceHeap(PriorityQueue<Integer> heap1, PriorityQueue<Integer> heap2) {
        if (heap1.size() < heap2.size()) {
            balanceHeap(heap2, heap1);
            return;
        }

        heap2.offer(heap1.poll());
    }

    // Returns the median of current data stream
    public double findMedian() {
        if (minHeap.size() == maxHeap.size()) {
            return (minHeap.peek() + maxHeap.peek()) / 2.0;
        } else if (minHeap.size() > maxHeap.size()) {
            return minHeap.peek();
        } else {
            return maxHeap.peek();
        }
    }
};

// Your MedianFinder object will be instantiated and called as such:
// MedianFinder mf = new MedianFinder();
// mf.addNum(1);
// mf.findMedian();
