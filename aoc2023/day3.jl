input = open("day3.txt") do f
    readlines(f)
end

example1 = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...\$.*....
.664.598.."""

function read_adjacent(lines)
    x = 1
    y = 1
    adjacent_nums = []

    while y <= length(lines)
        while x <= length(lines[y])
            if isdigit(lines[y][x])
                num = string(lines[y][x])
                i = 1
                adjacent = check_adjacent_symbol(lines, x, y)
                while x + i <= length(lines[y]) && isdigit(lines[y][x+i])
                    num *= string(lines[y][x+i])
                    adjacent = adjacent || check_adjacent_symbol(lines, x + i, y)
                    i += 1
                end
                if adjacent
                    push!(adjacent_nums, parse(Int, num))
                end
                x += i - 1
            end
            x += 1
        end
        x = 1
        y += 1
    end
    return reduce(+, adjacent_nums)
end


function check_adjacent_symbol(lines, x, y)::Bool
    if y > 1 && !isdigit(lines[y-1][x]) && lines[y-1][x] != '.'
        return true
    end

    if y < length(lines) && !isdigit(lines[y+1][x]) && lines[y+1][x] != '.'
        return true
    end

    if x > 1 && !isdigit(lines[y][x-1]) && lines[y][x-1] != '.'
        return true
    end

    if x < length(lines[y]) && !isdigit(lines[y][x+1]) && lines[y][x+1] != '.'
        return true
    end

    # diagonals
    if y > 1 && x > 1 && !isdigit(lines[y-1][x-1]) && lines[y-1][x-1] != '.'
        return true
    end

    if y > 1 && x < length(lines[y]) && !isdigit(lines[y-1][x+1]) && lines[y-1][x+1] != '.'
        return true
    end

    if y < length(lines) && x > 1 && !isdigit(lines[y+1][x-1]) && lines[y+1][x-1] != '.'
        return true
    end

    if y < length(lines) && x < length(lines[y]) && !isdigit(lines[y+1][x+1]) && lines[y+1][x+1] != '.'
        return true
    end

    return false
end

# println(read_adjacent(split(example1, '\n')))
println(read_adjacent(input))

# Part 2

function gear_ratios(lines)
    x = 1
    y = 1
    # location of gear to numbers around it
    gears = Dict{Tuple{Int,Int},Vector{Int}}()

    while y <= length(lines)
        while x <= length(lines)
            if lines[y][x] == '*'
                gears[(x, y)] = get_surrounding_numbers(lines, x, y)
            end
            x += 1
        end
        x = 1
        y += 1
    end

    # find all gears with 2 numbers
    two_gears = filter(gear -> length(gear[2]) == 2, gears)
    total = 0
    for lst in values(two_gears)
        total += reduce(*, lst)
    end
    return total
end

function get_surrounding_numbers(lines, x, y)
    surrounding = []
    looked_at = Set{Tuple{Int,Int}}()
    if !((x - 1, y - 1) in looked_at) && y > 1 && x > 1 && isdigit(lines[y-1][x-1])
        num, looked_at = find_num(lines, x - 1, y - 1)
        push!(surrounding, num)
        looked_at = union(looked_at, looked_at)
    end

    if !((x, y - 1) in looked_at) && y > 1 && isdigit(lines[y-1][x])
        num, looked_at = find_num(lines, x, y - 1)
        push!(surrounding, num)
        looked_at = union(looked_at, looked_at)
    end

    if !((x + 1, y - 1) in looked_at) && y > 1 && x < length(lines[y]) && isdigit(lines[y-1][x+1])
        num, looked_at = find_num(lines, x + 1, y - 1)
        push!(surrounding, num)
        looked_at = union(looked_at, looked_at)
    end

    if !((x + 1, y) in looked_at) && x < length(lines[y]) && isdigit(lines[y][x+1])
        num, looked_at = find_num(lines, x + 1, y)
        push!(surrounding, num)
        looked_at = union(looked_at, looked_at)
    end

    if !((x + 1, y + 1) in looked_at) && y < length(lines) && x < length(lines[y]) && isdigit(lines[y+1][x+1])
        num, looked_at = find_num(lines, x + 1, y + 1)
        push!(surrounding, num)
        looked_at = union(looked_at, looked_at)
    end

    if !((x, y + 1) in looked_at) && y < length(lines) && isdigit(lines[y+1][x])
        num, looked_at = find_num(lines, x, y + 1)
        push!(surrounding, num)
        looked_at = union(looked_at, looked_at)
    end

    if !((x - 1, y + 1) in looked_at) && y < length(lines) && x > 1 && isdigit(lines[y+1][x-1])
        num, looked_at = find_num(lines, x - 1, y + 1)
        push!(surrounding, num)
        looked_at = union(looked_at, looked_at)
    end

    if !((x - 1, y) in looked_at) && x > 1 && isdigit(lines[y][x-1])
        num, looked_at = find_num(lines, x - 1, y)
        push!(surrounding, num)
        looked_at = union(looked_at, looked_at)
    end
    return surrounding
end

function find_num(lines, x, y)
    num = string(lines[y][x])
    looked_at = Set{Tuple{Int,Int}}()
    push!(looked_at, (x, y))
    i = -1
    while x + i > 0 && isdigit(lines[y][x+i])
        num = string(lines[y][x+i]) * num
        push!(looked_at, (x + i, y))
        i -= 1
    end
    i = 1
    while x + i <= length(lines[y]) && isdigit(lines[y][x+i])
        num *= string(lines[y][x+i])
        push!(looked_at, (x + i, y))
        i += 1
    end
    return parse(Int, num), looked_at
end


# println(gear_ratios(split(example1, '\n')))
println(gear_ratios(input))