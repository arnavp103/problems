# Return the output array, and ignore all non-op characters
function deadfish(data)
    val = 0
    out = []
    for c in data
        if c == 'i'
            val += 1
        elseif c == 'd'
            val -= 1
        elseif c == 's'
            val *= val
        elseif c == 'o'
            push!(out, val)
        end
    end
    return out
end