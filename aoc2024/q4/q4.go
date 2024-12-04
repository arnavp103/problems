package main

import (
	"fmt"
	"os"
	"strings"
)

const Example = `MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX`

func parseInput(input string) [][]string {
	lines := strings.Split(input, "\n")
	// remove last newline if empty
	if lines[len(lines)-1] == "" {
		lines = lines[:len(lines)-1]
	}
	rows := make([][]string, len(lines))

	for i, line := range lines {
		// split line into columns
		rows[i] = strings.Split(line, "")
	}
	return rows
}

func part1(input string) {
	rows := parseInput(input)
	// XMAS can be written
	// horizontally as XMAS or backwards as SAMX
	// vertically as X or backwards as S
	//               M                 M
	//               A                 A
	//               S                 X
	// and diagonally in all 4 directions forwards and back

	num_xmas := 0

	// do all horizontal
	for _, row := range rows {
		for i := 0; i < len(row)-3; i++ {
			// forward
			if row[i] == "X" && row[i+1] == "M" && row[i+2] == "A" && row[i+3] == "S" {
				num_xmas++
			}
			// backward
			if row[i] == "S" && row[i+1] == "A" && row[i+2] == "M" && row[i+3] == "X" {
				num_xmas++
			}
		}
	}

	// do all vertical
	for i := 0; i < len(rows[0]); i++ {
		for j := 0; j < len(rows)-3; j++ {
			// forward
			if rows[j][i] == "X" && rows[j+1][i] == "M" && rows[j+2][i] == "A" && rows[j+3][i] == "S" {
				num_xmas++
			}
			// backward
			if rows[j][i] == "S" && rows[j+1][i] == "A" && rows[j+2][i] == "M" && rows[j+3][i] == "X" {
				num_xmas++
			}
		}
	}

	// topright bottom left
	for i := 0; i < len(rows)-3; i++ {
		for j := 0; j < len(rows[0])-3; j++ {
			// forward
			if rows[i][j] == "X" && rows[i+1][j+1] == "M" && rows[i+2][j+2] == "A" && rows[i+3][j+3] == "S" {
				num_xmas++
			}
			// backward
			if rows[i][j] == "S" && rows[i+1][j+1] == "A" && rows[i+2][j+2] == "M" && rows[i+3][j+3] == "X" {
				num_xmas++
			}
		}
	}

	// topleft bottom right
	for i := 0; i < len(rows)-3; i++ {
		for j := 3; j < len(rows[0]); j++ {
			// forward
			if rows[i][j] == "X" && rows[i+1][j-1] == "M" && rows[i+2][j-2] == "A" && rows[i+3][j-3] == "S" {
				num_xmas++
			}
			// backward
			if rows[i][j] == "S" && rows[i+1][j-1] == "A" && rows[i+2][j-2] == "M" && rows[i+3][j-3] == "X" {
				num_xmas++
			}
		}
	}

	fmt.Println(num_xmas)
}

func part2(input string) {
	rows := parseInput(input)
	num_xmas := 0
	// now we need to find all the MAS that form an X
	// S   S
	//   A        modulo the direction of the word
	// M   M

	// do all diagonal directions
	// first find all topleft bottom right diagonals
	for i := 1; i < len(rows)-1; i++ {
		for j := 1; j < len(rows[0])-1; j++ {
			// topleft to bottom right
			if rows[i-1][j-1] == "M" && rows[i][j] == "A" && rows[i+1][j+1] == "S" {
				// then check if the other diagonal is an MAS
				if rows[i+1][j-1] == "M" && rows[i-1][j+1] == "S" {
					num_xmas++
				}
				// and backwards
				if rows[i+1][j-1] == "S" && rows[i-1][j+1] == "M" {
					num_xmas++
				}
			}
			// bottom right to topleft
			if rows[i+1][j+1] == "M" && rows[i][j] == "A" && rows[i-1][j-1] == "S" {
				// then check if the other diagonal is an MAS
				if rows[i-1][j+1] == "M" && rows[i+1][j-1] == "S" {
					num_xmas++
				}
				// and backwards
				if rows[i-1][j+1] == "S" && rows[i+1][j-1] == "M" {
					num_xmas++
				}
			}
		}
	}

	fmt.Println(num_xmas)
}

func main() {
	part1(Example)
	part2(Example)

	var err error
	bytes, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	file := string(bytes)

	part1(file)
	part2(file)
}
