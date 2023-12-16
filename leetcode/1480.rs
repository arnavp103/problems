// 1480 running sum of 1-d array

impl Solution {
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
        let mut sum = 0;
        let mut run= vec![];
        for num in nums {
            sum += num;
            run.push(sum);
        }
        run
    }
}