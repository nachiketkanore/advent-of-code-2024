use anyhow::Result;
use regex::Regex;

fn main() -> Result<()> {
    let input = include_str!("3.in");
    let re_group = Regex::new(r"mul\((\d+),(\d+)\)")?; // regex groups
    let ans1 = re_group
        .captures_iter(input)
        .map(|caps| {
            (
                caps[1].parse::<i32>().unwrap(),
                caps[2].parse::<i32>().unwrap(),
            )
        })
        .fold(0, |ans, (a, b)| ans + a * b);

    dbg!(ans1);

    let re = Regex::new(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)")?;

    let mut enabled = true;

    let ans2 = re
        .find_iter(input)
        .map(|m| m.as_str())
        .map(|m| match &m[0..3] {
            "do(" => {
                enabled = true;
                0
            }
            "don" => {
                enabled = false;
                0
            }
            "mul" => {
                re_group
                    .captures_iter(m)
                    .map(|caps| {
                        (
                            caps[1].parse::<i32>().unwrap(),
                            caps[2].parse::<i32>().unwrap(),
                        )
                    })
                    .fold(0, |ans, (a, b)| ans + a * b)
                    * enabled as i32
            }
            _ => panic!("invalid regex match"),
        })
        .fold(0, |ans, val| ans + val);
    dbg!(ans2);

    Ok(())
}
