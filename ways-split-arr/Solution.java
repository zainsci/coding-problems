/**
 * source: https://leetcode.com/problems/number-of-ways-to-split-array/
 * provlem: https://leetcode.com/problems/number-of-ways-to-split-array/
 * site: LeetCode
 * type: Medium
 */

class Solution {
  public static void main(String[] args) {
    Solution sol = new Solution();

    int[] nums1 = { 10, 4, -8, 7 };
    System.out.println(sol.waysToSplitArray(nums1));

    int[] nums2 = { 2, 3, 1, 0 };
    System.out.println(sol.waysToSplitArray(nums2));

  }

  public int waysToSplitArray(int[] nums) {
    long count = 0;
    long totalSum = 0;
    long left = 0;

    for (int i : nums) {
      totalSum += i;
    }

    for (int i = 0; i < nums.length - 1; i++) {
      left += nums[i];

      if (left >= totalSum - left) {
        count++;
      }
    }

    return (int) count;
  }
}