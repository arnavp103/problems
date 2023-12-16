// 1071 gcd of a string

use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn gcd_of_strings(str1: String, str2: String) -> String {
        let mut res = String::new();
        let divisors1 = Solution::divisors(str1);
        let divisors2 = Solution::divisors(str2);
        for d in divisors1.intersection(&divisors2) {
            if d.len() > res.len() {
                res = d.clone();
            }
        }
        res
    }

    fn divisors(str: String) -> HashSet<String> {
        let mut res = HashSet::new();
        for i in 1..=str.len() {
            if str.len() % i == 0 {
                let cand = str[0..i].to_string();
                let mut dividing = true;

                let mut section = 0;
                while section * cand.len() < str.len() {
                    let start = section * cand.len();
                    let end = (section + 1) * cand.len();
                    if str[start..end] != cand {
                        dividing = false;
                        break;
                    }
                    section += 1;
                }

                if dividing {
                    res.insert(cand);
                }
            }
        }
        res
    }
}

fn main() -> () {
    let str1 = "ABCABC".to_string();
    let str2 = "ABC".to_string();
    let res = Solution::gcd_of_strings(str1, str2);
    println!("{}", res);

    let str1 = "ABABAB".to_string();
    let str2 = "ABAB".to_string();
    let res = Solution::gcd_of_strings(str1, str2);
    println!("{}", res); // AB

    let str1 = "LEET".to_string();
    let str2 = "CODE".to_string();
    let res = Solution::gcd_of_strings(str1, str2);
    println!("{}", res);

    let str1 = "ABCDEF".to_string();
    let str2 = "ABC".to_string();
    let res = Solution::gcd_of_strings(str1, str2);
    println!("{}", res);
}
