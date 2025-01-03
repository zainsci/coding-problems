/**
 * source: https://leetcode.com/problems/reverse-bits/
 * provlem: https://leetcode.com/problems/reverse-bits/
 * site: LeetCode
 * type: Easy
 */

public class Solution {
  public static void main(String[] args) {
    int num1 = 0b00000010100101000001111010011100;

    Solution solution = new Solution();
    int res = solution.reverseBits(num1);
    System.out.println(res);

    return;
  }

  public int reverseBits(int n) {
    String toBin = Integer.toBinaryString(n);
    StringBuilder bin32 = new StringBuilder(String.format("%32s", toBin).replace(" ", "0"));
    String revBin32 = bin32.reverse().toString();

    long res = Long.parseLong(revBin32, 2);
    return (int) res;
  }

  // Old Solution
  // public int reverseBits(int n) {
  // String toBin = Integer.toBinaryString(n);
  // String bin32 = String.format("%32s", toBin).replace(" ", "0");
  // System.out.println(bin32);

  // String reverseBin32 = "";

  // for (int i = bin32.length() - 1; i >= 0; i--) {
  // reverseBin32 = reverseBin32 + bin32.charAt(i);
  // }

  // long res = Long.parseLong(reverseBin32, 2);
  // return (int) res;
  // }
}