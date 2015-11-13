// https://leetcode.com/problems/roman-to-integer/

// Given a roman numeral, convert it to an integer.
// Input is guaranteed to be within the range from 1 to 3999.

public class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        map.put('I', new Integer(1));
        map.put('V', new Integer(5));
        map.put('X', new Integer(10));
        map.put('L', new Integer(50));
        map.put('C', new Integer(100));
        map.put('D', new Integer(500));
        map.put('M', new Integer(1000));
        int result = 0;
        while (s.length() >= 2){
            char leftC = s.charAt(0);
            char rightC = s.charAt(1);
            int leftN = map.get(leftC);
            int rightN = map.get(rightC);
            if (leftN < rightN){
                result = result + rightN - leftN;
                s = s.substring(2, s.length());
            }
            else if (leftN == rightN){
                result = result + rightN + leftN;
                s = s.substring(2, s.length());
            }
            else{
                result = result + leftN;
                s = s.substring(1, s.length());
            }
        }
        if (s.length() == 1){
            result = result + map.get(s.charAt(0));
        }
        return result;
    }
}