#! /bin/python3
from collections import deque

"""
source: https://leetcode.com/problems/number-of-recent-calls/
problem: https://leetcode.com/problems/number-of-recent-calls/
type: Easy 
site: LeetCode
"""


class RecentCounter:

    def __init__(self):
        self.curr_count = deque()

    def ping(self, t: int) -> int:
        self.curr_count.append(t)
        if len(self.curr_count) == 1:
            return 1

        while self.curr_count and self.curr_count[0] < t-3000:
            self.curr_count.popleft()

        return len(self.curr_count)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

def main():
    sol = RecentCounter()
    print(sol.ping(1))
    print(sol.ping(100))
    print(sol.ping(3001))
    print(sol.ping(3002))

    sol = RecentCounter()
    print(sol.ping(642))
    print(sol.ping(1849))  # [−1151, 1849]: 2
    print(sol.ping(4921))  # [1921, 4921]:
    print(sol.ping(5936))  # [2936, 5936]
    print(sol.ping(5957))  # [2957, 5957]


if __name__ == "__main__":
    main()
