use::std::collections::HashSet;


fn sieve_of_erastosthenes(n: u64) -> HashSet<u64> {
    let mut primes: HashSet<u64> = HashSet::new();
    let mut multiples: HashSet<u64> = HashSet::new();
    for i in 2..n+1 {
        if !multiples.contains(&i) {
            primes.insert(i);
            multiples.extend((i..n+1).filter(|x| x % i == 0)) }} 
    primes
}
