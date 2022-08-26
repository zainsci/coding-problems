#! /bin/python3

"""
source: https://techdevguide.withgoogle.com/paths/data-structures-and-algorithms/?no-filter=true
problem: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
type: easy
site: HackerRank
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
# import fileinput


def main():
    # input souce in hackerrank
    data = [
        "3",
        "sam 99912222",
        "tom 11122222",
        "harry 12299933",
        "sam",
        "edward",
        "harry",
    ]
    # comment out following if running on hackerrank
    # as well the import statement above
    # data = []
    # for line in fileinput.input():
    #     data.append(line.replace("\n", ""))
    count = int(data[0])
    source = data[1:count+1]
    to_check = data[count+1:]

    phone_book = {}
    for i in source:
        name, number = i.split(" ")
        phone_book[name] = number

    for i in to_check:
        if i in phone_book.keys():
            print(f"{i}={phone_book[i]}")
        else:
            print("Not Found")


if __name__ == "__main__":
    main()
