input = open("day7.txt") do file
    readlines(file)
end

example = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


function card_to_rank(card)
    # return 1 - 9
    # if alphabetic do T, J, Q, K, A = 10, 11, 12, 13, 14
    if isnumeric(card)
        return parse(Int, card)
    else
        return Dict('T' => 10, 'J' => 11, 'Q' => 12, 'K' => 13, 'A' => 14)[card]
    end
end


function parse_input(lines, card_rank)
    bets = []
    for line in lines
        hand, bid = split(line)
        push!(bets, ([card_rank(card) for card in collect(hand)], parse(Int, bid)))
    end
    return bets
end


function hand_type(hand)
    # check for 5 of a kind
    if length(unique(hand)) == 1
        return 7
    end
    # check for 4 of a kind
    for card in unique(hand)
        if count(x -> x == card, hand) == 4
            return 6
        end
    end
    # check for full house
    if length(unique(hand)) == 2
        return 5
    end
    # check for 3 of a kind
    for card in unique(hand)
        if count(x -> x == card, hand) == 3
            return 4
        end
    end
    # check for 2 pair
    if length(unique(hand)) == 3
        return 3
    end
    # check for 1 pair
    for card in unique(hand)
        if count(x -> x == card, hand) == 2
            return 2
        end
    end
    # else high card
    return 1
end

function is_less_than(hand1, hand2, hand_type=hand_type)
    if hand_type(hand2) == hand_type(hand1)
        # look for highest card
        for i in 1:5
            if hand2[i] > hand1[i]
                return true
            elseif hand2[i] < hand1[i]
                return false
            end
        end
        return false
    elseif hand_type(hand2) > hand_type(hand1)
        return true
    end
    return false
end


function total_winnings(bets)
    sorted_bets = sort(bets, by=x -> x[1], lt=is_less_than)
    winnings = 0
    for (rank, bet) in enumerate(sorted_bets)
        hand, bid = bet
        # println("rank: $rank, hand: $hand, bid: $bid")
        winnings += bid * rank
    end
    return winnings
end


# println(total_winnings(parse_input(split(example, "\n"), card_to_rank)))
println(total_winnings(parse_input(input, card_to_rank)))


# part 2

function joker_card_to_rank(card)
    # return 2 - 10
    # if alphabetic do T, J, Q, K, A = 11, 1, 12, 13, 14
    if isnumeric(card)
        return parse(Int, card) + 1
    else
        return Dict('T' => 11, 'J' => 1, 'Q' => 12, 'K' => 13, 'A' => 14)[card]
    end
end


# same as hand type but joker will impersonate another card
# to guarantee the highest possible hand type
# as long as the jokers become the most frequently occurring non-joker card
# the hand type is maximized
function joker_hand_type(hand)
    # sort hand based on how frequently each card occurs
    letter_counts = sort([(i, count(x -> x == i, hand)) for i in unique(hand)], by=x -> x[2], rev=true)
    if length(letter_counts) == 1
        # if there is only one card, it is a 5 of a kind
        return 7
    end
    most_freq_occuring = letter_counts[1][1]
    # if it's a J
    if most_freq_occuring == 1
        # make it the first non joker card
        # also why we checked to length to make sure this exists
        most_freq_occuring = letter_counts[2][1]
    end
    improved_hand = [c == 1 ? most_freq_occuring : c for c in hand]
    return hand_type(improved_hand)
end


function joker_winnings(bets)
    sorted_bets = sort(bets, by=x -> x[1], lt=(x, y) -> is_less_than(x, y, joker_hand_type))
    winnings = 0
    for (rank, bet) in enumerate(sorted_bets)
        hand, bid = bet
        # println("rank: $rank, hand: $hand, bid: $bid")
        winnings += bid * rank
    end
    return winnings
end

# println(joker_winnings(parse_input(split(example, "\n"), joker_card_to_rank)))
println(joker_winnings(parse_input(input, joker_card_to_rank)))