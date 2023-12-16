input = open("day5.txt") do file
    read(file, String)
end

example = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


function parse_input(input)
    # for each map, for each range in the map, (dest_start, (src_start, src_end))
    ranges = Vector{Vector{Tuple{Int,Tuple{Int,Int}}}}(undef, 7)
    seeds, maps... = split(input, "\n\n")
    _, seeds... = split(seeds)
    seeds = [parse(Int, seed) for seed in seeds]
    for (i, map) in enumerate(maps)
        ranges[i] = Vector{Tuple{Int,Tuple{Int,Int}}}(undef, 0)
        for line in split(strip(map), "\n")[2:end]
            line = split(line)
            dest_start = parse(Int, line[1])
            src_start = parse(Int, line[2])
            src_end = src_start + parse(Int, line[3]) - 1
            push!(ranges[i], (dest_start, (src_start, src_end)))
        end
    end
    return ranges, seeds
end

function lowest_location(maps, seeds)
    transformed_seeds = [seed for seed in seeds]
    for i in 1:length(seeds)
        for map in maps
            for (dest_start, (src_start, src_end)) in map
                if transformed_seeds[i] in src_start:src_end
                    transformed_seeds[i] = dest_start + transformed_seeds[i] - src_start
                    # println("seed $i transformed to $(transformed_seeds[i])")
                    break
                end
            end
        end
    end
    minimum(transformed_seeds)
end

# println(lowest_location(parse_input(example)...))
println(lowest_location(parse_input(input)...))

# Part 2

function transform_ranges(map_range, input_range, dest_start)
    # suppose map range has a bigger lower bound and a smaller upper bound compare to input range
    # then input range gets split into 3 parts:
    # before map range unchanged, inside map range which actually gets mapped, after map range unchanged

    # if something gets mapped its no longer eligible to get mapped again by another range in the same map
    # when we return we need to distinguish between ranges that got mapped and ranges that didn't
    # return tuple(unmapped_ranges, mapped_ranges)

    map_len = map_range[2] - map_range[1] + 1

    # if no overlap
    if input_range[2] < map_range[1] || input_range[1] > map_range[2]
        return ([input_range], [])
    end

    # if input range is completely inside map range
    if input_range[1] >= map_range[1] && input_range[2] <= map_range[2]
        return ([], [(dest_start + input_range[1] - map_range[1], dest_start + input_range[2] - map_range[1])])
    end

    # if map range is strictly inside input range
    if input_range[1] < map_range[1] && input_range[2] > map_range[2]
        pre = (input_range[1], map_range[1] - 1)
        post = (map_range[2] + 1, input_range[2])
        return ([pre, post], [(dest_start, dest_start + map_len - 1)])
    end

    # if input range overlaps with map range on the left
    if input_range[1] < map_range[1] && input_range[2] >= map_range[1] && input_range[2] <= map_range[2]
        pre = (input_range[1], map_range[1] - 1)
        return ([pre], [(dest_start, dest_start + (input_range[2] - map_range[1]))])
    end

    # if input range overlaps with map range on the right
    if input_range[1] >= map_range[1] && input_range[1] <= map_range[2] && input_range[2] > map_range[2]
        post = (map_range[2] + 1, input_range[2])
        return ([post], [(dest_start + (input_range[1] - map_range[1]), dest_start + map_len - 1)])
    end
end

function lowest_seed_ranges(maps, seeds)
    transformed = [[] for _ in 0:length(maps)]
    transformed[1] = [(s1, s1 + s2 - 1) for (s1, s2) in Iterators.partition(seeds, 2)]
    for (map_index, map) in enumerate(maps)
        out = []
        input_ranges = transformed[map_index]
        # the unmapped ranges - each map range may generate upto 2 unmapped ranges
        leftover = [input_ranges...]
        while length(leftover) > 0
            test = popfirst!(leftover)
            # if something doesnt get mapped at all we just pass it on to the next map
            changed = false
            # we need to keep track of whether anything got mapped at all
            # before appending to leftover
            to_add = Set{Tuple{Int,Int}}()
            for (dest_start, (src_start, src_end)) in map
                unmapped, mapped = transform_ranges((src_start, src_end), test, dest_start)

                union!(to_add, unmapped)
                append!(out, mapped)

                if mapped != []
                    changed = true
                    # dont remap an already mapped range
                    # remove yourself from to_add if you were there in from previous maps
                    if test in to_add
                        pop!(to_add, test)
                    end
                    break
                end
            end

            if !changed
                append!(out, [test])
            else
                append!(leftover, to_add)
            end
        end
        transformed[map_index+1] = out
    end
    minimum(map(first, transformed[end]))
end


# println(lowest_seed_ranges(parse_input(example)...))
println(lowest_seed_ranges(parse_input(input)...))