package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

const Example = `7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
89 88 86 85 82 83 79
8 6 4 4 1
1 3 6 7 9`

func parseInput(input string) [][]int {
	lines := strings.Split(input, "\n")
	// remove last newline if empty
	if lines[len(lines)-1] == "" {
		lines = lines[:len(lines)-1]
	}
	matrix := make([][]int, len(lines))

	for i, line := range lines {
		// split line into columns
		cols := strings.Fields(line)
		matrix[i] = make([]int, len(cols))
		for j, col := range cols {
			var err error
			matrix[i][j], err = strconv.Atoi(col)
			if err != nil {
				panic(err)
			}
		}
	}
	return matrix
}

// either all increasing or all decreasing
func monotonic(report []int) bool {
	all_increasing := true
	all_decreasing := true
	prev := report[0]
	for i := 1; i < len(report); i++ {
		if report[i] < prev {
			all_increasing = false
		}
		if report[i] > prev {
			all_decreasing = false
		}
		prev = report[i]
	}
	return all_increasing || all_decreasing
}

func is_safe(report []int) bool {
	prev := report[0]
	for i := 1; i < len(report); i++ {
		// any two adjacent levels differ by 1 <= x < 4
		diff := report[i] - prev
		if diff < 0 {
			diff = -diff
		}
		if diff > 3 || diff < 1 {
			return false
		}
		prev = report[i]
	}
	return true
}

func part1(input string) {
	num_safe := 0
	matrix := parseInput(input)

	for report_ind := 0; report_ind < len(matrix); report_ind++ {
		report := matrix[report_ind]
		if is_safe(report) && monotonic(report) {
			num_safe++
		}
	}

	fmt.Println(num_safe)
}

// either monotonic or if you can remove one element, it will be monotonic
func almost_monotonic(report []int) (bool, []int) {
	// check if it's already monotonic
	if monotonic(report) {
		return true, []int{}
	}
	almost_monotonic_report := make([]int, len(report)-1)
	can_be_monotonic := false
	possible_remove_ind := []int{}

	// check if removing one element makes it monotonic
	for i := 0; i < len(report); i++ {
		// remove element at index i
		for j := 0; j < len(report); j++ {
			if j < i {
				almost_monotonic_report[j] = report[j]
			} else if j > i {
				almost_monotonic_report[j-1] = report[j]
			}
		}
		if monotonic(almost_monotonic_report) {
			can_be_monotonic = true
			possible_remove_ind = append(possible_remove_ind, i)
		}
	}
	return can_be_monotonic, possible_remove_ind
}

// either is_safe or if you can remove one element, it will be safe
func almost_safe(report []int, remove_ind []int) bool {

	// check if it's already safe
	if is_safe(report) {
		return true
	}
	almost_safe_report := make([]int, len(report)-1)
	can_be_safe := false
	for _, remove_ind := range remove_ind {
		for j := 0; j < len(report); j++ {
			if j < remove_ind {
				almost_safe_report[j] = report[j]
			} else if j > remove_ind {
				almost_safe_report[j-1] = report[j]
			}
		}
		can_be_safe = can_be_safe || is_safe(almost_safe_report)
	}
	if len(remove_ind) != 0 {
		return can_be_safe
	}

	// check if removing one element makes it safe
	for i := 0; i < len(report); i++ {
		// remove element at index i
		for j := 0; j < len(report); j++ {
			if j < i {
				almost_safe_report[j] = report[j]
			} else if j > i {
				almost_safe_report[j-1] = report[j]
			}
		}

		if is_safe(almost_safe_report) {
			return true
		}
	}
	return false
}

func part2(input string) {
	num_safe := 0
	matrix := parseInput(input)

	for report_ind := 0; report_ind < len(matrix); report_ind++ {
		report := matrix[report_ind]
		is_monotonic, remove_ind := almost_monotonic(report)
		if is_monotonic && almost_safe(report, remove_ind) {
			// fmt.Println("safe", report)
			num_safe++
		}
	}
	fmt.Println(num_safe)
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
