#!/usr/bin/env python3

"""
source: 
problem: 
type: 
site: 
submission: 
"""


class Solution:
    # def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        count = 0
        boxes_o = []
        boxes_c = []

        for box in initialBoxes:
            if status[box] == 1:
                boxes_o.append(box)
            else:
                boxes_c.append(box)

        while boxes_o:
            boxes = set(boxes_c)

            for box in boxes_o:
                count += candies[box]
                for k in keys[box]:
                    status[k] = 1

                for b in containedBoxes[box]:
                    boxes.add(b)

            boxes_o, boxes_c = [], []
            for b in boxes:
                if status[b] == 1:
                    boxes_o.append(b)
                else:
                    boxes_c.append(b)

        return count


def main():
    sol = Solution()

    status = [1, 0, 1, 0]
    candies = [7, 5, 4, 100]
    keys = [[], [], [1], []]
    containedBoxes = [[1, 2], [3], [], []]
    initialBoxes = [0]
    print(sol.maxCandies(status, candies, keys, containedBoxes, initialBoxes))

    status = [1, 0, 0, 0, 0, 0]
    candies = [1, 1, 1, 1, 1, 1]
    keys = [[1, 2, 3, 4, 5], [], [], [], [], []]
    containedBoxes = [[1, 2, 3, 4, 5], [], [], [], [], []]
    initialBoxes = [0]
    print(sol.maxCandies(status, candies, keys, containedBoxes, initialBoxes))

    pass


if __name__ == "__main__":
    main()
