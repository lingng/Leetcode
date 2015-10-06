public class ReverseStr{
  public String reverseStr(String str){
    int len = str.length();
    StringBuilder sb = new StringBuilder();
    for (int i = len-1; i>=0; i--){
      sb.append(str.charAt(i));
    }
    return sb.toString(); 
  }
  
   public static void main(String[] args) throws Exception
   {
     ReverseStr r = new ReverseStr();
     System.out.println(r.reverseStr("abcde"));
   }
}