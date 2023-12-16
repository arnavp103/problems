// 1768 merge strings alternately

impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let mut res = word1
            .chars()
            .zip(word2.chars())
            .fold(String::new(), |mut acc, (c1, c2)| {
                acc.push(c1);
                acc.push(c2);
                acc
            });
        if word1.len() > word2.len() {
            res.push_str(&word1[word2.len()..]);
        } else {
            res.push_str(&word2[word1.len()..]);
        }
        res
    }
}
