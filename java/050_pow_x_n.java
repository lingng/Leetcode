// https://leetcode.com/problems/powx-n/
//
// Implement pow(x, n).

public class Solution {
    public double myPow(double x, int n) {
        if (n == 0){
            return 1.0;
        }
        if (n < 0){
            if (n == Integer.MIN_VALUE) {
                return 1;
            }
            return 1/this.myPow(x, -n);
        }
        if (n%2 == 0){
            return this.myPow(x*x, n/2);
        }
        else{
            return this.myPow(x*x, n/2)*x;
        }
    }
}
