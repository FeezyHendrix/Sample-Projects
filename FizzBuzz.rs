/*
Project: Mega Projects List - FizzBuzz
Author: Mandeep
Date: 10/22/2016

Problem: Write a program that prints the numbers from 1 to 100. 
For multiples of three print 'Fizz' instead of the number and for the multiples of five print 'Buzz'.
For numbers which are multiples of both three and five print 'FizzBuzz'.
*/

fn main() {
    for i in 1..100+1 {
        if i % 15 == 0 { println!("{}", "FizzBuzz"); }
        else if i % 5 == 0 { println!("{}", "Buzz"); }
        else if i % 3 == 0 { println!("{}", "Fizz"); }
        else { println!("{}", i); } } 
}