function ipsbetween(start, finish)
    (s1, s2, s3, s4) = split(start, '.') |> x -> (parse(Int64, x[1]), parse(Int64, x[2]), parse(Int64, x[3]), parse(Int64, x[4]))
    (f1, f2, f3, f4) = split(finish, '.') |> x -> (parse(Int64, x[1]), parse(Int64, x[2]), parse(Int64, x[3]), parse(Int64, x[4]))
    return (f1 - s1) * 256 * 256 * 256 + (f2 - s2) * 256 * 256 + (f3 - s3) * 256 + (f4 - s4)
end