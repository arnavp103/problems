
function largest_product(str, span)
    # check for invalid input
    if span < 0 || span > length(str)
        throw(ArgumentError("Invalid span"))
    end
    # check for empty string
    if length(str) == 0 && span > 0
        throw(ArgumentError("Invalid span"))
    end

    max = 0
    # create a sliding window of size span
    for series in ((@view str[i:i+span-1]) for i in 1:length(str)-span+1)
        println(series)
        # convert each series to an integer
        num = parse.(Int, collect(series))
        product = prod(num)
        if product > max
            max = product
        end
    end
    return max
end
