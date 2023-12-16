// 739 - daily temperatures

struct Solution;

impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        // traverse the array backwards and add every item to a stack
        // when we find an item with a higher temperature than the top of the stack
        // we pop the stack and increment the day counter by the popped day count
        let mut days = vec![0; temperatures.len()];
        let mut stack = vec![];
        for i in temperatures.iter().enumerate().rev() {
            let i = i.0;
            let mut day = 0;
            // if the current temperature is greater than the top of the stack
            // we pop the stack and increment the day counter by the popped stacks day count
            while !stack.is_empty() && temperatures[i] >= temperatures[*stack.last().unwrap()] {
                let temperature_index = stack.pop().unwrap();
                day += days[temperature_index];
            }

            if !stack.is_empty() {
                day += 1;
            } else {
                day = 0;
            }
            days[i] = day;
            stack.push(i);
        }
        days
    }
}

fn main() -> () {
    let temps = vec![73, 74, 75, 71, 69, 72, 76, 73];
    println!("{:?}", Solution::daily_temperatures(temps));
}
