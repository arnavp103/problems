struct RecentCounter {
    pings: Vec<i32>,
}

impl RecentCounter {
    fn new() -> Self {
        Self { pings: vec![] }
    }

    fn ping(&mut self, t: i32) -> i32 {
        self.pings.push(t);
        self.pings
            .iter()
            .rev()
            .take_while(|&x| t - x <= 3000)
            .count() as i32
    }
}
