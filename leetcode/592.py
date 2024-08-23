# 592 Fraction Addition and Subtraction

import math


class Rational:
    def __init__(self, fraction: str):
        self.numerator, self.denominator = map(int, fraction.split("/"))

    def __add__(self, other) -> "Rational":
        if self.denominator == other.denominator:
            return Rational(f"{self.numerator + other.numerator}/{self.denominator}")

        lcm = self.denominator * other.denominator
        numerator = (
            self.numerator * other.denominator + other.numerator * self.denominator
        )
        return Rational(f"{numerator}/{lcm}")

    def simplify(self) -> "Rational":
        gcd = math.gcd(self.numerator, self.denominator)
        return Rational(f"{self.numerator // gcd}/{self.denominator // gcd}")

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"


class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions: list["Rational"] = []
        start = 0
        for end, char in enumerate(expression):
            if char in "+-":
                if start == end:
                    continue
                fractions.append(Rational(expression[start:end]))
                start = end
        # add the final fraction
        fractions.append(Rational(expression[start:]))

        total = Rational("0/1")
        for fraction in fractions:
            total += fraction

        return str(total.simplify())
