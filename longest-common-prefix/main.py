#! /bin/python3

class Solution:
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    def longestCommonPrefix(self, strs):
        longest = strs[0]

        for str in strs:
            if len(str) <= len(longest):
                longest = longest[:len(str)]
            elif len(str) >= len(longest):
                longest = longest[:len(longest)]

            for i in range(len(longest)):
                if longest[i] != str[i]:
                    longest = longest[:i]
                    break

        return longest


def main():
    sol = Solution()

    strs = ["flower", "flow", "flight"]
    print(sol.longestCommonPrefix(strs))

    strs = ["dog", "racecar", "car"]
    print(sol.longestCommonPrefix(strs))

    return


if __name__ == "__main__":
    main()
