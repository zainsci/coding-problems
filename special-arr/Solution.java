/**
 * source: https://leetcode.com/problems/special-array-i/
 * provlem: https://leetcode.com/problems/special-array-i/
 * site: LeetCode
 * type: Easy
 * submission:
 * https://leetcode.com/problems/special-array-i/submissions/1527390543/
 */

class Solution {
  public static void main(String[] args) {
    int[] nums1 = { 1 };
    System.out.println(new Solution().isArraySpecial(nums1));

    int[] nums2 = { 2, 1, 4 };
    System.out.println(new Solution().isArraySpecial(nums2));

    int[] nums3 = { 4, 3, 1, 6 };
    System.out.println(new Solution().isArraySpecial(nums3));
  }

  public boolean isArraySpecial(int[] nums) {
    if (nums.length == 1)
      return true;

    for (int i = 0; i < nums.length - 1; i++) {
      if ((nums[i] + nums[i + 1]) % 2 == 0) {
        return false;
      }
    }

    return true;
  }
}