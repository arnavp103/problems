package main

import (
	"os"
	"sort"
	"strconv"
	"strings"
)

const Example = `3   4
4   3
2   5
1   3
3   9
3   3`

// parseInput returns sorted lists of integers (leftCol, rightCol) from the input string
func parseInput(input string) ([]int, []int) {
	lines := strings.Split(input, "\n")
	leftCol := make([]int, len(lines))
	rightCol := make([]int, len(lines))

	for i, line := range lines {
		if line == "" {
			continue
		}
		// split line into columns
		cols := strings.Fields(line)
		var err error
		leftCol[i], err = strconv.Atoi(cols[0])
		if err != nil {
			panic(err)
		}
		rightCol[i], err = strconv.Atoi(cols[1])
		if err != nil {
			panic(err)
		}

	}
	sort.Ints(leftCol)
	sort.Ints(rightCol)
	return leftCol, rightCol
}

func part1(input string) {
	leftCol, rightCol := parseInput(input)
	sum := 0

	for i := 0; i < len(leftCol); i++ {
		dist := leftCol[i] - rightCol[i]
		if dist < 0 {
			dist = -dist
		}
		sum += dist
	}
	println(sum)
}

func part2(input string) {
	// turn col2 into counter table
	leftCol, rightCol := parseInput(input)
	counter := make(map[int]int)
	for _, v := range rightCol {
		counter[v]++
	}

	sum := 0
	for _, v := range leftCol {
		val, present := counter[v]
		if present {
			sum += val * v
		}
	}
	println(sum)
}

func main() {
	// example := Example
	var err error
	bytes, err := os.ReadFile("input1.txt")
	if err != nil {
		panic(err)
	}
	file := string(bytes)

	// part1(example)
	part1(file)
	// part2(example)
	part2(file)
}
