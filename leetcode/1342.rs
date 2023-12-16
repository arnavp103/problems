// 1342 number of steps to reduce a num to zero

impl Solution {
	pub fn number_of_steps(mut num: i32) -> i32 {
		let mut steps = 0;
		let mut current = num;
		while current > 0 {
			if current % 2 == 0 {
				current /= 2;
			} else {
				current -= 1;
			}
			steps += 1;
		}
		steps
	}
	// other solution
	pub fn bitmask_num_of_steps(mut num: i32) -> i32 {
		let mut steps = 0;
		let mut current = num;
		while current > 0 {
			if current & 1 == 1 {
				current &= current - 1;
			} else {
				current = current >> 1;	// right shift by 1 bit = divide by 2
			}
			steps += 1;
		}
		steps
	}
}
