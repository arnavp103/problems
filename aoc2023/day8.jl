input = open("day8.txt") do f
    read(f, String)
end

example1 = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

example2 = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

function parse_input(lines)
    moves, rules = split(lines, "\n\n")
    nodes = Dict()
    for rule in split(rules, "\n")
        if rule == ""
            continue
        end
        name, children = split(rule, " = ")
        # remove parens
        children = children[2:end-1]
        # split on commas
        children = split(children, ", ")
        nodes[name] = children
    end
    return moves, nodes
end

function steps(moves, nodes)
    # start at root
    current = "AAA"
    steps = 0
    for move in Iterators.cycle(moves)
        children = nodes[current]
        if move == 'L'
            current = children[1]
        elseif move == 'R'
            current = children[2]
        end
        steps += 1

        if current == "ZZZ"
            return steps
        end
    end
end

# println(steps(parse_input(example1)...))
# println(steps(parse_input(example2)...))
println(steps(parse_input(input)...))

# part 2

example3 = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


# need to keep track of all cycles from each start point
function trace_path(nodes, moves, moveindex, start)
    current = start
    path = [(current, moveindex)]
    moveindexes = Iterators.Stateful(Iterators.rest(Iterators.cycle(1:length(moves)), moveindex))

    moveindex = popfirst!(moveindexes)
    while true
        sim_move = moves[moveindex]
        prev, _ = path[end]
        if sim_move == 'L'
            push!(path, (nodes[prev][1], moveindex))
        elseif sim_move == 'R'
            push!(path, (nodes[prev][2], moveindex))
        end
        # if we reach the start of the cycle, we're done
        if (path[end][1], moveindex) == path[1]
            path = path[1:end-1]
            break
        end
        moveindex = popfirst!(moveindexes)
    end
    # we no longer care about orientation in moves
    return map(pair -> pair[1], path)
end

function mod_solve(a, b, c, d)
    # solve a + bx = c mod d
    # x = (c - a) / b mod d
    # returns b * x
    remainder = c - a
    x = 0
    while mod(b * x, d) != remainder
        x += 1
        if x > 10000
            println("x > 10000")
            break
        end
    end
    return b * x
end

# assumes exactly one solution exists per path
function converge_to_z(moves, nodes)
    current = [node for node in keys(nodes) if node[end] == 'A']

    steps = 0
    moveindexes = Iterators.Stateful(Iterators.cycle(1:length(moves)))

    done = [false for _ in current]
    # dont count starting elems as visited
    # since they have no orientation in the moves
    # if we're in the same node with the same spot in the moves list we're cycling
    seen = [Set() for _ in current]
    # the cycle paths
    paths = [[] for _ in current]
    # where we are in the cycle
    # from 0 to length - 1 so we have to increment to get the exact index
    path_inds = [0 for _ in current]

    moveindex = popfirst!(moveindexes)

    for move in Iterators.cycle(moves)
        for (seen_ind, node) in enumerate(current)
            if done[seen_ind]
                path_inds[seen_ind] = (path_inds[seen_ind] + 1) % length(paths[seen_ind])
                continue
            end

            if move == 'L'
                current[seen_ind] = nodes[node][1]
            elseif move == 'R'
                current[seen_ind] = nodes[node][2]
            end
            new = current[seen_ind]
            if (new, moveindex) in seen[seen_ind]
                done[seen_ind] = true
                paths[seen_ind] = trace_path(nodes, moves, moveindex, new)
            else
                push!(seen[seen_ind], (new, moveindex))
            end
        end

        steps += 1

        if all(done)
            # now just cycle through the paths
            # taking steps that will leave the previous zs fixed
            step_mult = 1
            z_inds = [findfirst(path -> path[end] == 'Z', path) for path in paths]
            while any(pair -> paths[pair[1]][pair[2]+1][end] != 'Z', enumerate(path_inds))
                zdists = [mod(z_inds[ind] - (path_inds[ind] + 1), length(paths[ind])) for ind in eachindex(paths)]

                # ignore old 0s by making them large
                min_zdist, new_zero = findmin(zdist -> zdist == 0 ? 1000000 : zdist, zdists)

                jump = mod_solve(path_inds[new_zero], step_mult, path_inds[new_zero] + min_zdist, length(paths[new_zero]))

                for ind in eachindex(path_inds)
                    path_inds[ind] = (path_inds[ind] + jump) % length(paths[ind])
                end
                steps += jump
                step_mult = lcm(step_mult, length(paths[new_zero]))
            end

            return steps
        end

        # if we're done before cycling end early
        if all(node -> node[end] == 'Z', current)
            return steps
        end

        moveindex = popfirst!(moveindexes)
    end
end



# the cycle finding version actually breaks for example 3
# because some inputs cycle and others dont
# but when i find a cycle path i stop evaluating it
# println(converge_to_z(parse_input(example3)...))

println(converge_to_z(parse_input(input)...))
