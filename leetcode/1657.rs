use std::collections::{HashMap, HashSet};

struct Solution;

impl Solution {
    pub fn close_strings(word1: String, word2: String) -> bool {
        // get the frequency of each character in each word
        // if they have the same frequency of characters, then they are close

        let mut freq1 = HashMap::new();
        let mut freq2 = HashMap::new();

        word1
            .chars()
            .for_each(|c| *freq1.entry(c).or_insert(0) += 1);
        word2
            .chars()
            .for_each(|c| *freq2.entry(c).or_insert(0) += 1);

        println!("{:?}", freq1);
        println!("{:?}", freq2);

        let mut vals1 = freq1.values().collect::<Vec<_>>();
        let mut vals2 = freq2.values().collect::<Vec<_>>();

        vals1.sort();
        vals2.sort();

        let keys1 = freq1.keys().collect::<HashSet<_>>();
        let keys2 = freq2.keys().collect::<HashSet<_>>();

        vals1 == vals2 && keys1 == keys2
    }
}

fn main() {
    let word1 = "aaabbbbccddeeeeefffff";
    let word2 = "aaaaabbcccdddeeeeffff";
    println!(
        "{}",
        Solution::close_strings(word1.to_string(), word2.to_string())
    );
}
