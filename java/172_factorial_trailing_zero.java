// https://leetcode.com/problems/factorial-trailing-zeroes/

// Given an integer n, return the number of trailing zeroes in n!.
// Note: Your solution should be in logarithmic time complexity.

public class factorial_trailing_zero{
  public int zeros(int n) {
    int answer = 0;
    int x = 5;
    while (n >= x){
      answer = n / x;
      x = x * 5;
    }
        return answer;
    }
    
    public static void main(String[] args) throws Exception
    {
        factorial_trailing_zero a = new factorial_trailing_zero();
        System.out.println(a.zeros(6));
    }
}