function encode(s)
    out = ""
    if length(s) == 0
        return out
    end

    prev = s[1]
    count = 1
    
    for char in s[2:end]
        if char == prev
            count += 1
            continue
        end

        if count == 1
            out *= prev
        else
            out *= string(count)
            out *= prev
        end

        prev = char
        count = 1
    end

    if count == 1
        out *= prev
    else
        out *= string(count)
        out *= prev
    end
    

    return out
end



function decode(s)
    out = ""
    num = "0"
    for char in s
        if isnumeric(char)
            num *= char
            continue
        end 

        if num == "0"
            out *= char
        else
            n = parse(Int64, num)
            out *= repeat(char, n)
            num = "0"
        end
    end
    return out
end

using Test

@testset "encode strings" begin

    @test encode("") == ""

    @test encode("XYZ") == "XYZ"

    @test encode("AABBBCCCC") == "2A3B4C"

    @test encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB") == "12WB12W3B24WB"

    @test encode("aabbbcccc") == "2a3b4c"

    @test encode("  hsqq qww  ") == "2 hs2q q2w2 "

end


@testset "decode strings" begin

    @test decode("") == ""

    @test decode("XYZ") == "XYZ"

    @test decode("2A3B4C") == "AABBBCCCC"

    @test decode("12WB12W3B24WB") == "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"

    @test decode("2a3b4c") == "aabbbcccc"

    @test decode("2 hs2q q2w2 ") == "  hsqq qww  "

end

@testset "encode then decode" begin

    @test decode(encode("zzz ZZ  zZ")) == "zzz ZZ  zZ"

end
