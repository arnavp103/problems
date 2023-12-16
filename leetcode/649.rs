// 649 Dota2 Senate

// "RD" -> "Radiant"
// "RDD" -> "Dire"
// Always ban the upcoming enemy senator

use std::collections::VecDeque;

impl Solution {
    pub fn predict_party_victory(senate: String) -> String {
        let mut radiant = VecDeque::new();
        let mut dire = VecDeque::new();
        for (i, c) in senate.chars().enumerate() {
            if c == 'R' {
                radiant.push_back(i);
            } else {
                dire.push_back(i);
            }
        }

        while !radiant.is_empty() && !dire.is_empty() {
            let r = radiant.pop_front().unwrap();
            let d = dire.pop_front().unwrap();
            if r < d {
                radiant.push_back(r + senate.len());
            } else {
                dire.push_back(d + senate.len());
            }
        }
        if radiant.is_empty() {
            "Dire".to_string()
        } else {
            "Radiant".to_string()
        }
    }
}
