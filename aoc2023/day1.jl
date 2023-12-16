input = open("day1.txt") do file
    readlines(file)
end

example1 = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

function first_and_last_digit_sum(lines)
    digits = map(line -> filter(isdigit, line), lines)
    reduce(+, map(digs -> parse(Int, digs[1] * digs[end]), digits))
end

# println(first_and_last_digit_sum(split(example1, '\n')))
println(first_and_last_digit_sum(input))

# Part 2

example2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

function numberize_line(line)
    convert = Dict("one" => "1", "two" => "2", "three" => "3", "four" => "4", "five" => "5", "six" => "6", "seven" => "7", "eight" => "8", "nine" => "9")
    out = ""

    for (index, letter) in enumerate(line)
        if isdigit(letter)
            out *= letter
            continue
        end

        for (word, number) in convert
            if index + length(word) - 1 <= length(line) && line[index:index+length(word)-1] == word
                out *= number
                break
            end
        end
    end
    out
end

function first_and_last_digit_sum2(lines)
    digits = numberize_line.(lines)
    reduce(+, map(digs -> parse(Int, digs[1] * digs[end]), digits))
end

# println(first_and_last_digit_sum2(split(example2, '\n')))
println(first_and_last_digit_sum2(input))