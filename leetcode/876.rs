// 876 middle of a linked list

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}

impl Solution {
    pub fn middle_node(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
		let mut length = 0;
		let mut current = &head;
		while let Some(node) = current {
			length += 1;
			current = &node.next;
		}
		let mut middle = head;
		for i in 1..(length/2)+1 {	// returns 3 for 5, 4 for 6, etc
			match middle {
				Some(node) => {
					middle = node.next;
				},
				None => return None,
			}
		}
		middle	// this is a bad solution because it destroys head
		// we can't recover head since we didn't take its reference and moved it directly
	}
	// clever solution (not tested)
	pub fn fast_and_slow(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
		let mut slow = &head;
		let mut fast = &head;
		while let Some(node) = fast {
			fast = &node.next;	// fast moves first here then below
			if let Some(node) = fast {
				fast = &node.next;	// fast moves twice as fast as slow so slow will be in the middle when fast reaches the end
				slow = &slow.as_ref().unwrap().next;
			}
		}
		slow.clone()
	}
}