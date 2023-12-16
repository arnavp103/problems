// There is a game played on a grid of squares with one piece which is initially located at a position (m, n) of
// a grid (with m, n ∈ N). The grid’s origin (0, 0) is at the bottom left corner and it is arbitrarily large including
// all squares with pairs of natural number coordinates.
// The game is played between two players, who take alternate turns to move this game piece towards the
// origin. The valid moves for the piece are like a chess queen, as long as the direction of the move is towards
// the origin, i.e. left, down or diagonally towards left-down. Like a chess queen, the piece is allowed to travel
// as far as the player chooses in a valid direction during the one move. The player that moves the piece to the
// origin wins the game. Below is an example play of the game:
// 3
// played from the initial location (8, 6) where the first player loses the game.
// We say a player has a winning strategy for a game iff there is play for this player to win this game
// independent of the choices that the opponent makes. For example, the first player always has a winning
// strategy from any location (n, 0), (0, n), or (n, n) because the player can move the piece in one move to the
// origin and win.
// A two-player game is called determined if from any given position, exactly one of the players has a winning
// strategy. The above game is determined. Given two excellent players and any location (m, n), either player
// one always wins the game from (m, n) or he always loses.
// The goal of this exercise is to implement a decision procedure. The input will be the pair of numbers
// (m, n). The output is “1” if the first player has a winning strategy from this location, and “2” if the second
// player has a winning strategy from this location.
// Note: this problem is not a random implementation problem. To come up with a solution that scales up, you
// are encouraged to think carefully about how checking for the existence of a winning strategy relates to the
// concepts of existential and universal path properties. You are also encouraged to think about the algorithm
// we discussed for until and how the idea behind that algorithm can hint at a nice solution for this problem.

// bottom up dynamic programming

// first start by splliting the map into just the bottom right triangle
// remember when we cancel out rows to cancel out the row corresponding to the flipped value though

// first add 0, 0 to the diagonal blocker and 0 to the row blocker
// anything on these squares is winning for p1
// now we start iterating from the lowest unblocked row
// inner loop from the first non diagonally blocked square in the row
// so x + 2, y + 1 is the first non diagonally blocked square in the first row above the last diagonal
// once you're on a row that and square thats not blocked
// add it to diagonal blocker and row blocker
// add the inverted form y,x to row blocker
// if at any point we're on a blocker square and curr_x > x || curr_y > y then p1 wins
// if curr_x == x && curr_y == y then p2 wins

use std::collections::HashSet;

fn winner(x: u64, y: u64) -> char {
    if y > x {
        return winner(y, x);
    }

    let mut diagonal_blocker = (0, 0);
    let mut row_blocker = HashSet::new();
    row_blocker.insert(0);

    let mut rank = 0;
    let mut file = 0;

    while rank <= y {
        if row_blocker.contains(&rank) {
            rank += 1;
            row_blocker.remove(&rank);
            continue;
        }

        while file <= x {
            let height_diff = rank - diagonal_blocker.1;
            if file <= diagonal_blocker.0 + height_diff {
                file = diagonal_blocker.0 + height_diff + 1;
                continue;
            }

            diagonal_blocker = (file, rank);
            row_blocker.insert(rank);
            row_blocker.insert(file);

            if rank == y && file == x {
                return '2';
            }
            break;
        }
        rank += 1;
    }
    '1'
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let x = args[1].parse::<u64>();
    let y = args[2].parse::<u64>();

    let x = x.expect("x must be a natural number");
    let y = y.expect("y must be a natural number");

    println!("{}", winner(x, y));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(winner(0, 0), '1');
    }

    #[test]
    fn test_2() {
        assert_eq!(winner(1, 0), '1');
    }

    #[test]
    fn test_3() {
        assert_eq!(winner(0, 1), '1');
    }

    #[test]
    fn test_4() {
        assert_eq!(winner(1, 1), '1');
    }

    #[test]
    fn test_7() {
        assert_eq!(winner(2, 2), '1');
    }

    #[test]
    fn test_6() {
        assert_eq!(winner(1, 2), '2');
    }

    #[test]
    fn test_8() {
        assert_eq!(winner(2, 1), '2');
    }

    #[test]
    fn test_9() {
        assert_eq!(winner(5, 3), '2');
    }

    #[test]
    fn test_10() {
        assert_eq!(winner(7, 4), '2');
    }

    #[test]
    fn test_11() {
        assert_eq!(winner(10, 6), '2');
    }

    #[test]
    fn test_12() {
        assert_eq!(winner(13, 8), '2');
    }

    #[test]
    fn test_13() {
        assert_eq!(winner(15, 9), '2');
    }

    #[test]
    fn test_14() {
        assert_eq!(winner(18, 11), '2');
    }

    #[test]
    fn test_15() {
        assert_eq!(winner(20, 12), '2');
    }

    #[test]
    fn test_16() {
        assert_eq!(winner(23, 14), '2');
    }

    #[test]
    fn test_17() {
        assert_eq!(winner(26, 16), '2');
    }

    #[test]
    fn test_18() {
        assert_eq!(winner(28, 17), '2');
    }

    #[test]
    fn test_19() {
        assert_eq!(winner(31, 19), '2');
    }

    #[test]
    fn test_20() {
        assert_eq!(winner(34, 21), '2');
    }

    #[test]
    fn test_21() {
        assert_eq!(winner(36, 22), '2');
    }

    #[test]
    fn test_22() {
        assert_eq!(winner(39, 24), '2');
    }

    #[test]
    fn test_23() {
        assert_eq!(winner(41, 25), '2');
    }

    #[test]
    fn test_24() {
        assert_eq!(winner(44, 27), '2');
    }

    #[test]
    fn test_25() {
        assert_eq!(winner(47, 29), '2');
    }

    #[test]
    fn test_26() {
        assert_eq!(winner(49, 30), '2');
    }

    #[test]
    fn test_27() {
        assert_eq!(winner(52, 32), '2');
    }

    #[test]
    fn test_28() {
        assert_eq!(winner(54, 33), '2');
    }

    #[test]
    fn test_29() {
        assert_eq!(winner(57, 35), '2');
    }

    #[test]
    fn test_30() {
        assert_eq!(winner(60, 37), '2');
    }

    #[test]
    fn test_31() {
        assert_eq!(winner(62, 38), '2');
    }

    #[test]
    fn test_32() {
        assert_eq!(winner(65, 40), '2');
    }

    #[test]
    fn test_33() {
        assert_eq!(winner(68, 42), '2');
    }

    #[test]
    fn test_34() {
        assert_eq!(winner(70, 43), '2');
    }

    #[test]
    fn test_35() {
        assert_eq!(winner(73, 45), '2');
    }

    #[test]
    fn test_36() {
        assert_eq!(winner(75, 46), '2');
    }

    #[test]
    fn test_37() {
        assert_eq!(winner(78, 48), '2');
    }

    #[test]
    fn test_38() {
        assert_eq!(winner(81, 50), '2');
    }

    #[test]
    fn test_39() {
        assert_eq!(winner(83, 51), '2');
    }

    #[test]
    fn test_40() {
        assert_eq!(winner(86, 53), '2');
    }

    #[test]
    fn test_41() {
        assert_eq!(winner(89, 55), '2');
    }

    #[test]
    fn test_42() {
        assert_eq!(winner(91, 56), '2');
    }

    #[test]
    fn test_43() {
        assert_eq!(winner(94, 58), '2');
    }

    #[test]
    fn test_44() {
        assert_eq!(winner(96, 59), '2');
    }

    #[test]
    fn test_45() {
        assert_eq!(winner(99, 61), '2');
    }
}
