// convert a number between 1 and 31 to binary
// for each 1 add an action
// 00001 = wink
// 00010 = double blink
// 00100 = close your eyes
// 01000 = jump
// 10000 = Reverse the order of the operations in the secret handshake.
pub fn actions(n: u8) -> Vec<&'static str> {
    let mut v = Vec::new();
    if n & 0b00001 != 0 {
        v.push("wink");
    }
    if n & 0b00010 != 0 {
        v.push("double blink");
    }
    if n & 0b00100 != 0 {
        v.push("close your eyes");
    }
    if n & 0b01000 != 0 {
        v.push("jump");
    }
    if n & 0b10000 != 0 {
        v.reverse();
    }
    v
}
