// 643 Maximum Average Subarray

impl Solution {
    pub fn find_max_average(nums: Vec<i32>, k: i32) -> f64 {
        let mut sum = 0;
        for i in 0..k {
            sum += nums[i as usize];
        }
        let mut max = sum;
        for i in k..nums.len() as i32 {
            sum += nums[i as usize] - nums[(i - k) as usize];
            if sum > max {
                max = sum;
            }
        }
        max as f64 / k as f64
    }
}
