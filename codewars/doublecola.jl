names = ["sheldon", "leonard", "penny", "rajesh", "howard"]

# extra comma to clarify that the first arg is a tuple
doublegroup = ((name, n),) -> (name, 2n)

function doublecola(n)
    grouped = [(name, 1) for name in names]

    while n > 0
        n -= grouped[1][2]
        if n <= 0
            return grouped[1][1]
        end
        push!(grouped, doublegroup(popfirst!(grouped)))
    end
end

println(doublecola(10010))

using Test

@test doublecola(1) == "sheldon"

@test doublecola(6) == "sheldon"

@test doublecola(10010) == "howard"