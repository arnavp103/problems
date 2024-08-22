# 1009 Complement of Base 10 Integer
# apparently this is the same question as 476


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # copied from 476
        bin_repr = bin(n)
        # ditch the 0b prefix
        digits = list(bin_repr[2:])

        for i, digit in enumerate(digits):
            digits[i] = "0" if digit == "1" else "1"

        inverse = "".join(digits)
        return int(inverse, 2)
