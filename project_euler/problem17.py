"""
If the numbers 1 to 5 are written out in words:
one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive
were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains
23 letters and 115 (one hundred and fifteen) contains 20 letters.
"""

number_letters = {
    0: 4,  # zero
    1: 3,  # one
    2: 3,  # two
    3: 5,  # three
    4: 4,  # four
    5: 4,  # five
    6: 3,  # six
    7: 5,  # seven
    8: 5,  # eight
    9: 4,  # nine
    10: 3,  # ten
    11: 6,  # eleven
    12: 6,  # twelve
    13: 8,  # thirteen
    14: 8,  # fourteen
    15: 7,  # fifteen
    16: 7,  # sixteen
    17: 9,  # seventeen
    18: 8,  # eighteen
    19: 8,  # nineteen
    20: 6,  # twenty
    30: 6,  # thirty
    40: 5,  # forty
    50: 5,  # fifty
    60: 5,  # sixty
    70: 7,  # seventy
    80: 6,  # eighty
    90: 6,  # ninety
    100: 7,  # hundred
    1000: 8,  # thousand
}


def solution(s: int, n: int) -> int:
    """return the number of letters used to write out the numbers from s to n"""

    def number_to_letters(n: int) -> int:
        """return the number of letters used to write out n"""
        if n == 1000:
            return 3 + 8  # one + thousand
        if n == 100:
            return 3 + 7  # one + hundred

        if n in number_letters:
            return number_letters[n]
        if n < 100:
            return number_letters[n - n % 10] + number_letters[n % 10]
        if n < 1000:
            if n % 100 == 0:
                return number_letters[n // 100] + number_letters[100]
            return (
                number_letters[n // 100]
                + number_letters[100]
                + 3  # and
                + number_to_letters(n % 100)
            )

        print(n // 1000)
        return number_letters[n // 1000] + number_letters[1000]

    return sum(number_to_letters(i) for i in range(s, n + 1))


print(solution(1, 1000))

# 21124 - correct
