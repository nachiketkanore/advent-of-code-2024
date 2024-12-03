fn main() {
    let input = include_str!("1.in");
    let mut first = vec![];
    let mut second = vec![];

    input
        .trim()
        .split('\n')
        .map(|line| {
            let vals: Vec<i32> = line.split("   ").map(|val| val.parse().unwrap()).collect();
            (vals[0], vals[1])
        })
        .for_each(|(a, b)| {
            first.push(a);
            second.push(b);
        });

    first.sort();
    second.sort();

    let ans1 = first
        .iter()
        .zip(second.clone())
        .fold(0, |ans, (a, b)| ans + (a - b).abs());

    dbg!(ans1);

    let ans2 = first.iter().fold(0, |ans, a| {
        ans + a * second.iter().filter(|b| a == *b).count() as i32
    });

    dbg!(ans2);
}
