use rand::Rng;
use std::collections::HashSet;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let args = std::env::args().collect::<Vec<String>>();
    if args.len() < 2 {
        println!("Usage: {} <file> [t=1000]", args[0]);
        return;
    }

    let file = File::open(&args[1]);
    let file = match file {
        Ok(f) => f,
        Err(e) => {
            println!("Error opening file: {}", e);
            return;
        }
    };

    // default t is 1000, make it higher for a better estimate
    let mut t = 1000;
    if args.len() > 2 {
        t = args[2].parse::<usize>().unwrap_or(100);
    }

    println!("Estimating {} distinct words", cvm(file, t));
    #[cfg(debug_assertions)]
    println!("Naive unique words: {}. ", naive_unique_words(&args[1]));
}

fn cvm(file: File, t: usize) -> usize {
    let reader = BufReader::new(file);

    // caching the rng makes it faster
    let mut rng = rand::thread_rng();

    // the core cvm algorithm
    let mut seen = HashSet::new();
    let mut p: f64 = 1.0;

    for line in reader.lines() {
        let line = line.expect("Error reading line");
        let words = line.split_whitespace();

        for word in words {
            // first remove the element from the set
            seen.remove(word);
            // add word to seen with probability p
            if rng.gen::<f64>() < p {
                seen.insert(word.to_string());
                if seen.len() >= t {
                    // remove elements with probability 1/2
                    let mut new_seen = HashSet::new();
                    for s in seen.into_iter() {
                        if rng.gen::<f64>() > 0.5 {
                            new_seen.insert(s);
                        }
                    }
                    seen = new_seen;
                    p = p / 2.0;
                }
            }
        }
    }

    (seen.len() as f64 / p) as usize
}

fn naive_unique_words(file: &str) -> usize {
    let file = File::open(file).expect("Error opening file");
    let reader = BufReader::new(file);
    let mut words = HashSet::new();
    for line in reader.lines() {
        let line = line.expect("Error reading line");
        let words_in_line = line.split_whitespace();
        for word in words_in_line {
            words.insert(word.to_string());
        }
    }
    words.len()
}
