# 211 Design Add and Search Words Data Structure


class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node["sentinel"] = True

    def search(self, word: str) -> bool:
        return self.search_helper(word, self.root)

    def search_helper(self, word: str, node: dict) -> bool:
        if len(word) == 0:
            return "sentinel" in node

        letter = word[0]
        if letter != ".":
            if letter not in node:
                return False
            return self.search_helper(word[1:], node[letter])

        for possible_node in node.values():
            # if possible_node is a sentinel, then skip it
            # can't just `if possible_node`
            # because possible node is also a dictionary which is truthy
            if possible_node == True:
                continue

            if self.search_helper(word[1:], possible_node):
                return True

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
