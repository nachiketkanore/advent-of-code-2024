fn check(vals: &mut Vec<i32>) -> bool {
    let ok1 = vals.is_sorted();
    vals.reverse();
    let ok2 = vals.is_sorted();
    let mut ok3 = true;
    for i in 1..vals.len() {
        ok3 &= (vals[i - 1] - vals[i]).abs() > 0 && (vals[i - 1] - vals[i]).abs() < 4;
    }
    (ok1 || ok2) && ok3
}
fn main() {
    let ans1 = include_str!("2.in")
        .trim()
        .split('\n')
        .filter(|line| {
            let mut vals = line
                .split(' ')
                .map(|v| v.parse::<i32>().unwrap())
                .collect::<Vec<i32>>();
            check(&mut vals)
        })
        .count();
    dbg!(ans1);

    let ans2 = include_str!("2.in")
        .trim()
        .split('\n')
        .filter(|line| {
            let vals = line
                .split(' ')
                .map(|v| v.parse::<i32>().unwrap())
                .collect::<Vec<i32>>();
            (0..vals.len())
                .map(|i| {
                    let mut nvals = vals
                        .iter()
                        .enumerate()
                        .filter(|(id, _)| *id != i)
                        .map(|(_, val)| *val)
                        .collect::<Vec<i32>>();
                    check(&mut nvals) as i32
                })
                .sum::<i32>()
                > 0
        })
        .count();
    dbg!(ans2);
}
