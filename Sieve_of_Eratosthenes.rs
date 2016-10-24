use::std::collections::HashSet;


fn sieve_of_erastosthenes(n: i64) -> HashSet<i64> {
    let mut primes: HashSet<i64> = HashSet::new();
    let mut multiples: HashSet<i64> = HashSet::new();
    for i in 2..n+1 {
        if !multiples.contains(&i) {
            primes.insert(i);
            multiples.extend((i..n+1).filter(|x| x % i == 0)) }} 
    primes
}
