// 167 two sum II - input array is sorted

impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut res = vec![];
        let mut i = 0;
        let mut j = numbers.len() - 1;
        while i < j {
            let sum = numbers[i] + numbers[j];
            if sum == target {
                res.push(i as i32 + 1);
                res.push(j as i32 + 1);
                break;
            } else if sum < target {
                i += 1;
            } else {
                j -= 1;
            }
        }
        res
    }
}
