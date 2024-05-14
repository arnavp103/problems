// 3075 Maximize Happiness of Selected Children

impl Solution {
    pub fn maximum_happiness_sum(happiness: Vec<i32>, k: i32) -> i64 {
        /*
        We basically have to pick the largest values. Order matters right?

        Consider the array [3, 2, 0] we could do 3 -> 1 (since decremented)
        or we could do 2 -> 2
        So actually order doesn't matter in this case.

        But what about [3, 3, 1, 0] with k = 3
        Here we can select 3 -> 2 -> 0 which is better than 1 -> 2 -> 1

        So it seems like just selecting the top k in order works.
         */
        let mut happiness_sum: i64 = 0;
        let mut selected = 0;

        let mut happiness = happiness;
        // descending sort
        happiness.sort();
        happiness.reverse();

        if k <= 0 {
            return 0;
        }

        for i in 0..k {
            let happy = happiness[i as usize] - selected;
            if happy < 0 {
                break;
            }
            selected += 1;
            happiness_sum += happy as i64;
        }
        happiness_sum
    }
}
