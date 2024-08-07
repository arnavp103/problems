# 273 Integer to English Words


class Solution:
    def numberToWords(self, num: int) -> str:
        # constraints
        # 0 <= num <= 2^31 - 1 (2_147_483_647)
        if num == 0:
            return "Zero"

        names = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion",
            1000000000000: "Trillion",
        }

        words = []

        def to_words(n):
            if n == 0:
                return
            if n <= 20:
                words.append(names[n])
            elif n < 100:
                words.append(names[(n // 10) * 10])
                to_words(n % 10)
            elif n < 1_000:
                words.append(names[n // 100])
                words.append(names[100])
                to_words(n % 100)
            elif n < 1_000_000:
                to_words(n // 1000)
                words.append(names[1000])
                to_words(n % 1000)
            elif n < 1_000_000_000:
                to_words(n // 1_000_000)
                words.append(names[1_000_000])
                to_words(n % 1_000_000)
            elif n < 1_000_000_000_000:
                to_words(n // 1_000_000_000)
                words.append(names[1_000_000_000])
                to_words(n % 1_000_000_000)
            else:
                to_words(n // 1_000_000_000_000)
                words.append(names[1_000_000_000_000])
                to_words(n % 1_000_000_000_000)

        to_words(num)
        return " ".join(words)
