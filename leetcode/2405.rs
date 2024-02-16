// 2405 Optimal Partition of String

// Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

// Return the minimum number of substrings in such a partition.

// Note that each character should belong to exactly one substring in a partition.

impl Solution {
    pub fn partition_string(s: String) -> i32 {
        let mut partition = String::from("");
        let mut count = 1;
        for c in s.chars() {
            if partition.contains(c) {
                count += 1;
                partition = String::from(c);
            } else {
                partition.push(c.clone());
            }
        }
        count
    }
}
