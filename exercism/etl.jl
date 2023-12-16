# performing a transfrom on the data



input = Dict(1 => ['A', 'E', 'I', 'O', 'U'])

function transform(input::AbstractDict)
    output = Dict()
    for (key, value) in input
        for letter in value
            output[lowercase(letter)] = key
        end
    end
    return output
end




output = Dict('a' => 1, 'e' => 1, 'i' => 1, 'o' => 1, 'u' => 1)

