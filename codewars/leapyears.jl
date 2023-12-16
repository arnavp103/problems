function isleapyear(year::Integer)::Bool
    return year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)
end