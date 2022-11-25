#! /bin/python3

"""
source: https://leetcode.com/problems/build-array-from-permutation
problem: https://leetcode.com/problems/build-array-from-permutation
type: easy
site: LeetCode
"""

class Solution:
    # def buildArray(self, nums: List[int]) -> List[int]:
    def buildArray(self, nums) :
      new_arr = [None for _ in nums]
      
      for i in range(len(nums)):
        new_arr[i] = nums[nums[i]]

      return new_arr

def main():
  sol = Solution()

  nums = [0,2,1,5,3,4]
  print(sol.buildArray(nums))
  
  nums = [5,0,1,2,3,4]
  print(sol.buildArray(nums))

  return 


if __name__ == "__main__": 
  main()