#! /bin/python3

"""
source: https://leetcode.com/problems/string-compression/
problem: https://leetcode.com/problems/string-compression/
type: Medium
site: LeetCode
"""


class Solution:
    # def compress(self, chars: List[str]) -> int:
    def compress(self, chars):
        if len(chars) == 1:
            return len(chars)

        char = chars[0]
        char_count = 0
        root_idx = 0

        for i in range(len(chars)):
            if char != chars[i]:
                chars[root_idx] = char
                root_idx += 1
                char = chars[i]

                if char_count != 1:
                    char_count_str = str(char_count)
                    for num in char_count_str:
                        chars[root_idx] = num
                        root_idx += 1

                char_count = 1

            else:
                char_count += 1

        chars[root_idx] = char
        root_idx += 1
        char_count_str = str(char_count)
        if char_count != 1:
            for num in char_count_str:
                chars[root_idx] = num
                root_idx += 1

        chars = chars[:root_idx]
        print(chars[:root_idx])
        return len(chars)


def main():
    sol = Solution()

    chars = ["a", "a", "b", "b", "c", "c", "c"]
    print(sol.compress(chars))

    chars = ["a"]
    print(sol.compress(chars))

    chars = ["a", "b", "b", "b", "b", "b",
             "b", "b", "b", "b", "b", "b", "b"]
    print(sol.compress(chars))

    chars = ["a", "a", "a", "b", "b", "a", "a"]
    print(sol.compress(chars))

    chars = ["a", "b", "c"]
    print(sol.compress(chars))

    return


if __name__ == "__main__":
    main()
