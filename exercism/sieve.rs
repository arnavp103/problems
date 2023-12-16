// sieve of eratosthenes
pub fn primes_up_to(upper_bound: u64) -> Vec<u64> {
    let mut primes: Vec<u64> = Vec::new();
    // we test all the numbers from 2 to upper_bound.
    let mut sieve: Vec<bool> = vec![true; upper_bound as usize + 1];
    for i in 2..=upper_bound {
        if sieve[i as usize] {
            primes.push(i);
            for j in (i * 2..=upper_bound).step_by(i as usize) {
                sieve[j as usize] = false;
            }
        }
    }
    primes
}
