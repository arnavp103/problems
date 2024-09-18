# 884 Uncommon Words from Two Sentences
# https://leetcode.com/problems/uncommon-words-from-two-sentences/ - Easy


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        once: set[str] = set()
        twice: set[str] = set()

        words = s1.split(" ")
        words2 = s2.split(" ")

        words.extend(words2)

        for word in words:
            if word in twice:
                continue

            if word in once:
                once.remove(word)
                twice.add(word)
                continue

            # word never seen
            once.add(word)

        return list(once)
