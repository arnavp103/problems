// 735 asteroid collision

struct Solution;

impl Solution {
    pub fn asteroid_collision(asteroids: Vec<i32>) -> Vec<i32> {
        let mut stack = vec![];

        if asteroids.len() == 0 {
            return stack;
        }

        for asteroid in asteroids {
            if stack.len() == 0 {
                stack.push(asteroid);
                continue;
            }

            let mut top = stack.last().unwrap().clone();
            let topsign = top.signum();
            let asign = asteroid.signum();

            if topsign == -1 && asign == 1 {
                stack.push(asteroid);
                continue;
            }

            if topsign == asign {
                stack.push(asteroid);
                continue;
            }

            if topsign == 1 && asign == -1 {
                if top.abs() < asteroid.abs() {
                    while top.signum() == topsign && top.abs() < asteroid.abs() {
                        stack.pop();
                        if stack.len() == 0 || stack.last().unwrap().signum() == asign {
                            stack.push(asteroid);
                            break;
                        }
                        top = *stack.last().unwrap_or(&0);
                    }
                }

                if top.abs() == asteroid.abs() {
                    stack.pop();
                    continue;
                }

                if top.abs() > asteroid.abs() {
                    continue;
                }
            }
        }

        stack
    }
}

fn main() {
    let asteroids = vec![10, 2, -5];
    let res = Solution::asteroid_collision(asteroids);
    println!("{:?}", res);

    let asteroids = vec![-2, -2, 1, -2];
    let res = Solution::asteroid_collision(asteroids);
    println!("{:?}", res);

    let asteroids = vec![1, 2, 3, -4];
    let res = Solution::asteroid_collision(asteroids);
    println!("{:?}", res);

    let asteroids = vec![-2, 2, 1, -2];
    let res = Solution::asteroid_collision(asteroids);
    println!("{:?}", res);
}
