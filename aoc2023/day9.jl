input = open("day9.txt") do file
    readlines(file)
end

example1 = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


function parse_input(lines)
    return map(line -> parse.(Int, split(line)), lines)
end


# history for: 1 3 6 10 15 21
# take the difference of the lower row[x] and lower row[x + 1]
# if out of bounds just stop the array there
# 1  1  1   1 na na
# 2  3  4   5  6 na
# 1  3  6  10 15 21
# once all values are the same, push that value until original reading length
# backsolve for next reading by doing current row[x] + upper row[x] = current row[x+1]
# 1  1  1   1  1  1
# 2  3  4   5  6  7
# 1  3  6  10 15 21 28 <- final extrapolation
function extrapolate_reading(reading)
    history = [reading]
    # while the top values of history are not all equal
    while !all(val -> history[1][1] == val, history[1])
        new_reading = [history[1][2] - history[1][1]]
        for i in 2:length(history[1])-1
            push!(new_reading, history[1][i+1] - history[1][i])
        end
        pushfirst!(history, new_reading)
    end
    history[1] = repeat([history[1][1]], length(reading))
    # map(println, history)
    y = 2
    while y < length(history)
        x = length(history[y])
        while x < length(reading)
            push!(history[y], history[y][x] + history[y-1][x])
            x += 1
        end
        y += 1
    end
    return history[end][end] + history[end-1][end]
end

function total_readings(readings)
    sum(extrapolate_reading.(readings))
end

ex = parse_input(split(example1, "\n"))
println(total_readings(ex))
println(total_readings(parse_input(input)))

# part 2 pretty much the same thing
#    (2) (2)  2   2   2    2
#    (-4)(-2) 0   2   4    6
#    (5)  3   3   5   9   15
# (5) 10  13  16  21  30  45
function extrapolate_history(reading)
    history = [reading]
    while !all(val -> history[1][1] == val, history[1])
        new_reading = [history[1][2] - history[1][1]]
        for i in 2:length(history[1])-1
            push!(new_reading, history[1][i+1] - history[1][i])
        end
        pushfirst!(history, new_reading)
    end
    history[1] = repeat([history[1][1]], length(reading))
    y = 2
    while y < length(history)
        x = length(history[y])
        while x < length(reading)
            # index thats directly above you if you add to the left
            # since above row is always length reading
            ind = length(reading) - x + 1
            pushfirst!(history[y], history[y][1] - history[y-1][ind])
            x += 1
        end
        y += 1
    end
    # map(println, history)
    return history[end][1] - history[end-1][1]
end

function total_history(readings)
    sum(extrapolate_history.(readings))
end

println(total_history(ex))
println(total_history(parse_input(input)))