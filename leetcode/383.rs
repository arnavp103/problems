// 383 Ransom Note
use std::collections::HashMap;

impl Solution{
	pub fn can_construct(ransom_note: String, magazine: String) -> bool {
		let mut letters = HashMap::new();
		for c in magazine.chars() {
			// entry returns a mutable reference at that key's value or a fail
			// or_insert inserts the value if it doesn't exist and fails
			let count = letters.entry(c).or_insert(0);
			*count += 1;	// reference the object itself
		}
		for c in ransom_note.chars() {
			match letters.get_mut(&c) {
				Some(count) => {
					*count -= 1;
					if *count < 0 {
						return false;
					}
				},
				None => return false,
			}
		}
		true
	}
}
















