
function sum_of_multiples(limit, factors)
    sum = 0
    # julia ranges are inclusive
    for i in 1:limit-1
        for factor in factors
            if factor != 0 && i % factor == 0
                sum += i
                # to avoid duplicates
                break
            end
        end
    end
    return sum
end
