function divisors(n)
    divisors = [1, n]

    for i in 2:floor(Int, sqrt(n))
        if n % i == 0
            push!(divisors, i)
            push!(divisors, n ÷ i)
        end
    end

    return length(unique(divisors))
end