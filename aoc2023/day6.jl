input = open("day6.txt") do file
    readlines(file)
end

example = """
Time:      7  15   30
Distance:  9  40  200"""


function parse_input(lines)
    time, distance = lines
    time = parse.(Int, split(time)[2:end])
    distance = parse.(Int, split(distance)[2:end])
    return zip(time, distance)
end

function ways_to_win(td_pair)
    time, distance = td_pair
    ways = 0
    for time_held in 1:time
        remaining_time = time - time_held
        speed = time_held
        dist = speed * remaining_time
        if dist > distance
            ways += 1
        end
    end
    return ways
end

function solve(lines)
    td_pairs = parse_input(lines)
    ways = map(ways_to_win, td_pairs)
    return prod(ways)
end

# println(solve(split(example, "\n")))
println(solve(input))


# part 2

function big_race(lines)
    time, distance = lines
    time = parse(Int, reduce(*, split(time)[2:end]))
    distance = parse(Int, reduce(*, split(distance)[2:end]))
    return ways_to_win((time, distance))
end

# println(big_race(split(example, "\n")))
println(big_race(input))