public class ReverseArray{
  public int[] reverseArr(int[] arr){
    int len = arr.length;
    for (int i = 0; i < len/2; i++){
      int tmp = arr[i];
      arr[i] = arr[len-1-i];
      arr[len-1-i] = tmp;
    }
    return arr;
  }
  
  public static void main(String[] args){
    ReverseArray r = new ReverseArray();
    int[] arr = new int[4];
    for (int i = 0; i < 4; i++){
      arr[i] = i;
    }
    arr = r.reverseArr(arr);
    int len = arr.length;
    for (int i = 0; i < len; i++){
      System.out.println(arr[i]);
    }
  }
}