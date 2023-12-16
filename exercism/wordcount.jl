
# return a dict of words and their counts
# contractions count as seperate words
# punctuation is ignored
# case is ignored
# eg: "That's the password: 'PASSWORD 123'!", cried the Special Agent.\nSo I fled.
# returns Dict("that's"=>1,"the"=>2,"password"=>2,"123"=>1,"cried"=>1,"special"=>1,"agent"=>1,"so"=>1,"i"=>1,"fled"=>1)


function wordcount(sentence)
    # remove all punctuation
    # regex is match all non alphanumeric characters and non apostrophe
    # turn punctuation to whitespace to split on
    words = replace(sentence, r"[^[:alnum:]']" => " ")

    # split on whitespace
    words = split(words)

    # keep apostrophe only if they're in a contraction, so surrounded by letters
    # check if apostrophe is in a contraction
    words = map(w ->
            if occursin(r"[a-zA-Z]'[a-zA-Z]", w)
                w
            else
                replace(w, "'" => "")
            end, words)

    words = lowercase.(words)
    words = filter(x -> x != "" && x != "'", words)

    word_counts = Dict()
    for word in words
        word_counts[word] = get(word_counts, word, 0) + 1
    end
    return word_counts
end
