public class Solution {
    public boolean wordPattern(String pattern, String str) {
        String[] words = str.split(" ");
        if (words.length != pattern.length())
            return false;
        Map index = new HashMap();
        for (int i=0; i<words.length; ++i)
            if (!Objects.equals(index.put(pattern.charAt(i), i),index.put(words[i], i)))
                return false;
        return true;
    }
    
    public boolean wordPattern1(String pattern, String str){
        String[] words = str.split(" ");
        if (pattern.length() != words.length){
            return false;
        }
        if (pattern.length() == 0 || pattern.length() == 1){
            return true;
        }

        HashMap< Character , String> dict = new HashMap<Character, String>();
        for (int i = 0; i < pattern.length(); i++){
            String tmp = dict.get(pattern.charAt(i));
            if (tmp != null){
                if (!words[i].equals(tmp)){
                    return false;
                }
            }
            else{
                dict.put(pattern.charAt(i), words[i]);
            }
        }
        dict.clear();
        
        HashMap<String, Character> dict1 = new HashMap<String, Character>();
        for (int i = 0; i < pattern.length(); i++){
            Character tmp = dict1.get(words[i]);
            if (tmp != null){
                if (pattern.charAt(i) != tmp){
                    return false;
                }
            }
            else{
                dict1.put(words[i], pattern.charAt(i));
            }
        }
        return true;
    }
    
    public static void main(String[] args){
        word_pattern w1 = new word_pattern();
        System.out.println(w1.wordPattern("abba", "dog cat cat dog"));
    }
}