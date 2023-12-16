input = open("day4.txt") do f
    readlines(f)
end

example = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

function parse_input(input)
    cards = []
    for line in input
        winning = Set()
        winning_nums, nums = strip.(split(line, " | "))
        winning_nums = split(split(winning_nums, ": ")[2], " ")
        for num in winning_nums
            if num == ""
                continue
            end
            push!(winning, parse(Int, num))
        end
        recieved = [parse(Int, num) for num in split(nums, " ") if num != ""]
        push!(cards, (winning, recieved))
    end
    return cards
end

function total_score(cards)
    score = 0
    for card in cards
        power = count(num -> num in card[1], card[2]) - 1
        score += power >= 0 ? 2^power : 0
    end
    return score
end

# println(total_score(parse_input(split(example, "\n"))))
println(total_score(parse_input(input)))

# Part 2

function total_scratchcards(cards)
    # card: (Set(41 48 83 86 17), [83 86  6 31 17  9 48 53])
    # one copy of each card
    copies = [1 for card in cards]
    for (index, card) in enumerate(cards)
        won = count(num -> num in card[1], card[2])
        for i in 1:won
            if index + i > length(copies)
                break
            end
            copies[i+index] += copies[index]
        end
    end
    sum(copies)
end

# println(total_scratchcards(parse_input(split(example, "\n"))))
println(total_scratchcards(parse_input(input)))