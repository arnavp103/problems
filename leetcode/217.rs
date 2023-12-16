//217 contains duplicate

impl Solution {
	// 1. sort the array
	// 2. iterate through the array and check if the current element is equal to the next element
	// faster than o(n^2) solution where we double for loop over each element
	pub fn contains_duplicate(nums: Vec<i32>) -> bool {
		let mut nums = nums;
		nums.sort();
		for i in 0..nums.len() - 1 {
			if nums[i] == nums[i + 1] {
				return true;
			}
		}
		false
	}
}