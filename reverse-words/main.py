#! /bin/python3
class Solution:
    def reverseWords(self, s):
        return " ".join([x for x in s.split(" ")[::-1] if x != ""])


def main():
    sol = Solution()
    s = "the sky is blue"
    print(sol.reverseWords(s))

    s = "  hello world  "
    print(sol.reverseWords(s))

    s = "a good   example"
    print(sol.reverseWords(s))

    return


if __name__ == "__main__":
    main()
