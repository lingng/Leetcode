// https://leetcode.com/problems/sqrtx/
//
// Implement int sqrt(int x).
// Compute and return the square root of x.

public class Solution {
    public int mySqrt(int x) {
        if (x == 0) {
            return 0;
        }
        long low = 1;
        long high = x / 2 + 1;
        while (low < high) {
            long mid = low + (high - low) / 2;
            long curr = mid * mid;
            if (curr == x) {
                return (int) mid;
            } else if (curr > x) {
                if (mid - 1 < 2 || (mid - 1) * (mid - 1) < x) {
                    return (int) mid - 1;
                } else {
                    high = mid - 1;
                }
            } else {
                if (mid + 1 > (x/2 + 1) || (mid + 1) * (mid + 1) > x) {
                    return (int) mid;
                } else {
                    low = mid + 1;
                }
            }
        }

        return (int) low;
    }
}
