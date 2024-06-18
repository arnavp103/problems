"""
Using problem22_names.txt, a 46K text file containing
over five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""


def solution() -> int:
    """return the total of all the name scores in the file"""
    with open("problem22_names.txt", encoding="utf-8") as file:
        names = file.read().replace('"', "").split(",")
    names.sort()
    return sum(
        (i + 1) * sum(ord(char) - 64 for char in name) for i, name in enumerate(names)
    )


print(solution())

# 871198282 - correct
