# 476 Number Complement
# apparently this is the same question as 1009


class Solution:
    def findComplement(self, num: int) -> int:
        bin_repr = bin(num)
        # ditch the 0b prefix
        digits = list(bin_repr[2:])

        for i, digit in enumerate(digits):
            digits[i] = "0" if digit == "1" else "1"

        inverse = "".join(digits)
        return int(inverse, 2)
