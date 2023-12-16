input = open("day2.txt") do file
    readlines(file)
end

example1 = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

function parse_inp(lines)::Vector{Vector{Vector{Int}}}
    # result is a vector of games
    out = Vector{Vector{Vector{Int}}}()
    for line in lines
        # each game is a vector of hands
        game = Vector{Vector{Int}}()

        _, hands = split(line, ':')
        for hand in split(hands, ';')
            # each hand shown is [r, g, b]
            shown = [0, 0, 0]
            pairs = strip.(split(hand, ','))
            for pair in pairs
                amount, color = split(pair)
                color = strip(color)[1]
                if color == 'r'
                    shown[1] += parse(Int, amount)
                elseif color == 'g'
                    shown[2] += parse(Int, amount)
                elseif color == 'b'
                    shown[3] += parse(Int, amount)
                end
            end
            push!(game, shown)
        end
        push!(out, game)
    end
    out
end


function possible_sum(games::Vector{Vector{Vector{Int}}}, max_hand::Vector{Int})
    legals = findall(game -> all(hand -> hand[1] <= max_hand[1] && hand[2] <= max_hand[2] && hand[3] <= max_hand[3], game), games)
    # get the sum of their indexes
    reduce(+, legals)
end

max_hand = [12, 13, 14]

# println(possible_sum(parse_inp(split(example1, '\n')), max_hand))
println(possible_sum(parse_inp(input), max_hand))


# Part 2

# same example

function minimum_possible_hand(games::Vector{Vector{Vector{Int}}})
    total = 0
    for game in games
        max_r = reduce(max, map(hand -> hand[1], game))
        max_g = reduce(max, map(hand -> hand[2], game))
        max_b = reduce(max, map(hand -> hand[3], game))
        total += reduce(*, [max_r, max_g, max_b])
    end
    total
end

# println(minimum_possible_hand(parse_inp(split(example1, '\n'))))
println(minimum_possible_hand(parse_inp(input)))