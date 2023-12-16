// 392 is subsequence

impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        let mut s = s.chars().peekable();
        for c in t.chars() {
            if let Some(&c2) = s.peek() {
                if c == c2 {
                    s.next();
                }
            }
        }
        s.next().is_none()
    }
}
