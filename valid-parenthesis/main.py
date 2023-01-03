#! /bin/python3


class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        stack = []
        opening = ["(", "{", "["]
        closing = [")", "}", "]"]
        parens = {"[": "]", "{": "}", "(": ")", "]": "[", "}": "{", ")": "("}

        for paren in s:
            if paren in opening:
                stack.append(paren)
            elif paren in closing:
                if len(stack) == 0:
                    return False

                if stack[-1] == parens[paren]:
                    stack.pop()
                else:
                    return False

        if len(stack) > 0:
            return False

        return True


def main():
    sol = Solution()
    s = "("
    s = ")"
    print(sol.isValid(s))

    s = "()[]{}"
    print(sol.isValid(s))


if __name__ == "__main__":
    main()
