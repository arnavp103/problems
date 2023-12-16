//53 maximum subarray

impl Solution {
    // for every sub array of length 2 -> n - 1, we can add it to the hashmap and use dynamic programming
    // to find the maximum subarray
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut max = nums[0];
        // let mut start = 0;
        // let mut size = 1;
        for i in 0..nums.len() {
            // get the sum of the subarray
            let subsum: i32 = nums[i..].iter().sum();
            if nums[i] > max {
                max = nums[i];
            } else if nums[i] < 0 {
                continue;
            }
            let mut j = nums.len() - 1;
            while j > i {
                if nums[j] < 0 {
                    j -= 1;
                    continue;
                }
                let sum: i32 = nums[i..j + 1].iter().sum();
                if sum > max {
                    max = sum;
                    // start = i;
                    // size = j - i + 1;
                }
                j -= 1;
            }
        }
        max
    }
}
