# 49 Group Anagrams

from collections import Counter


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        freqs = [Counter(s) for s in strs]

        unique_freqs = set()
        for freq in freqs:
            unique_freqs.add(tuple(sorted(freq.items())))

        anagrams = {freq: [] for freq in unique_freqs}
        for i, freq in enumerate(freqs):
            anagrams[tuple(sorted(freq.items()))].append(strs[i])

        return list(anagrams.values())
