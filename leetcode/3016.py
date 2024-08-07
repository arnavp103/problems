# 3016 Minimum Number of Pushes to Type Word II

from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        # there's eight different keys we can map to
        # since there's 26 letters we need |-26/8-| = 4 presses
        one_presses = set()
        two_presses = set()
        three_presses = set()
        presses = 0

        counts = Counter(word)
        sorted_chars = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        for c, count in sorted_chars:
            if c in one_presses:
                presses += count
            elif len(one_presses) < 8:
                one_presses.add(c)
                presses += count
            elif c in two_presses:
                presses += 2 * count
            elif len(two_presses) < 8:
                two_presses.add(c)
                presses += 2 * count
            elif c in three_presses:
                presses += 3 * count
            elif len(three_presses) < 8:
                three_presses.add(c)
                presses += 3 * count
            else:
                presses += 4 * count

        return presses
