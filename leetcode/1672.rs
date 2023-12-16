// 1672 Richest Customer Wealth

impl Solution {
    pub fn maximum_wealth(accounts: Vec<Vec<i32>>) -> i32 {
        let mut max = 0;
        for wealth in accounts {
            let totalwealth: i32 = wealth.iter().sum();
            max = if totalwealth > max {totalwealth} else {max};
        }
        max
    }
}