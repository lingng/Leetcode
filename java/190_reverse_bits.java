// https://leetcode.com/problems/reverse-bits/

// Reverse bits of a given 32 bits unsigned integer.
// For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
// Follow up:
// If this function is called many times, how would you optimize it?

public class reverse_bits{
    public int reverseBits(int n) {
        int res = 0;
        for(int i = 0; i < 32; i++) {
            res <<= 1;
            res |= n & 1;
            n >>= 1;
        }

        return res;
    }
    
    public static void main(String[] args) throws Exception
    {
        reverse_bits a = new reverse_bits();
        System.out.println(a.reverseBits(1));
    }
}