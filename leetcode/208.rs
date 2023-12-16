// 208 - Implement Trie (Prefix Tree)

use std::collections::HashMap;

struct TrieNode {
    leaf: bool,
    // k - way split from each node
    children: HashMap<char, TrieNode>,
}

struct Trie {
    root: TrieNode,
}

impl Trie {
    fn new() -> Self {
        Trie {
            root: TrieNode {
                leaf: false,
                children: HashMap::new(),
            },
        }
    }

    fn insert(&mut self, word: String) {
        let mut node = &mut self.root;
        for c in word.chars() {
            node = node.children.entry(c).or_insert(TrieNode {
                leaf: false,
                children: HashMap::new(),
            });
        }
        node.leaf = true;
    }

    fn search(&self, word: String) -> bool {
        let mut node = &self.root;
        for c in word.chars() {
            if let Some(child) = node.children.get(&c) {
                node = child;
            } else {
                return false;
            }
        }
        node.leaf
    }

    fn starts_with(&self, prefix: String) -> bool {
        let mut node = &self.root;
        for c in prefix.chars() {
            if let Some(child) = node.children.get(&c) {
                node = child;
            } else {
                return false;
            }
        }
        // if we get here, then we have found the prefix
        true
    }
}
