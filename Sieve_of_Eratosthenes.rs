#![feature(step_by)] // Unstable features allows stepping through iterator
use::std::collections::HashSet;


fn sieve_of_erastosthenes(n: i32) -> HashSet<i32> {
    let mut primes: HashSet<i32> = HashSet::new();
    let mut multiples: HashSet<i32> = HashSet::new();
    for i in 2..n+1 {
        if !multiples.contains(&i) {
            primes.insert(i);
            multiples.extend((i..n+1).step_by(i)) }} 
    primes
}
