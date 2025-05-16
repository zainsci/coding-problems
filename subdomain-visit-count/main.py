#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/subdomain-visit-count/
problem: https://leetcode.com/problems/subdomain-visit-count/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/subdomain-visit-count/submissions/1635411443/
"""


class Solution:
    # def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
    def subdomainVisits(self, cpdomains):
        count = {}

        for x in cpdomains:
            c, d = x.split(" ")[0], x.split(" ")[1]
            deps = d.split(".")

            for y in range(len(deps)):
                dom = ".".join(deps[y:])

                if dom in count.keys():
                    count[dom] += int(c)
                else:
                    count[dom] = int(c)

        return [f"{count[x]} {x}" for x in count.keys()]


def main():
    sol = Solution()

    cpdomains = ["9001 discuss.leetcode.com"]
    print(sol.subdomainVisits(cpdomains))

    cpdomains = ["900 google.mail.com", "50 yahoo.com",
                 "1 intel.mail.com", "5 wiki.org"]
    print(sol.subdomainVisits(cpdomains))

    pass


if __name__ == "__main__":
    main()
