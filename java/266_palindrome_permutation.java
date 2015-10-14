// Given a string, determine if a permutation of the string could form a palindrome.

// For example,
// "code" -> False, "aab" -> True, "carerac" -> True.

// Hint:

// Consider the palindromes of odd vs even length. What difference do you notice?
// Count the frequency of each character.
// If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?


import java.util.*;

public class palindrome_permutation{
  public boolean palindrome(String s){
    HashMap<Character, Integer> dic = new HashMap<Character, Integer>();
    int len = s.length();
    for (int i = 0; i < len; i++){
      if (dic.containsKey(s.charAt(i))){
        dic.remove(s.charAt(i));
      }
      else{
        dic.put(s.charAt(i), 1);
      }
    }
    if (len % 2 == 0){
      if (dic.size() == 0){
        return true;
      }
      else{
        return false;
      }
    }
    else{
      if (dic.size() == 1){
        return true;
      }
      else{
        return false;
      }
    }
    
  }
  public static void main(String[] args){
      palindrome_permutation p = new palindrome_permutation();
      String s = "aaabb";
      System.out.println(p.palindrome(s));
  }
}