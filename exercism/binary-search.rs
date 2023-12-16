pub fn find(array: &[i32], key: i32) -> Option<usize> {
    let size = array.len();
    let mut left = 0;
    let mut right = size - 1;

    let mut prev_mid = i32::MAX;
    while left <= right {
        // if left and right don't change after an iteration, (perhaps they're both 0)
        // then end the loop
        let mid = left + ((right - left) / 2);
        if mid == prev_mid {
            return None;
        }
        if array[mid] == key {
            return Some(mid);
        } else if array[mid] < key {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
        prev_mid = mid;
    }
    None
}
