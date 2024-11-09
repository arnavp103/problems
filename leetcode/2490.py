# # 2580 Circular Sentence
# https://leetcode.com/problems/circular-sentence/ - Easy

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        is_circular = True
        words = sentence.split()
        for i in range(len(words)):
            if words[i][-1] != words[(i+1) % len(words)][0]:
                is_circular = False
                break
        return is_circular