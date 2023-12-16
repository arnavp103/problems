module Solution
export rgb

function rgb(r, g, b)
    r, g, b = clamp.((r, g, b), 0, 255)
    return string.((r, g, b), base=16, pad=2) |> join |> uppercase
end
end