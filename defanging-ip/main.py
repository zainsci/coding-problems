#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/defanging-an-ip-address/
problem: https://leetcode.com/problems/defanging-an-ip-address/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/defanging-an-ip-address/submissions/1623914303/
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        i = 0
        ans = ""

        while i < len(address):
            if address[i] == ".":
                ans += "[.]"
                i += 1
            else:
                ans += address[i]
                i += 1

        return ans


def main():
    sol = Solution()

    address = "1.1.1.1"
    print(sol.defangIPaddr(address))

    address = "255.100.50.0"
    print(sol.defangIPaddr(address))

    pass


if __name__ == "__main__":
    main()
